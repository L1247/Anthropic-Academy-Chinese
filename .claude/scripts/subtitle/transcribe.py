"""faster-whisper 包裝：音訊抽取 + 轉錄 → SRT。"""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from srt_utils import Cue, format_timecode, write_srt


def extract_audio(video_path: Path, wav_path: Path) -> None:
    """用 FFmpeg 從影片抽取 16kHz mono PCM WAV（Whisper 最佳輸入）。"""
    cmd = [
        "ffmpeg",
        "-y",           # 覆寫輸出
        "-i", str(video_path),
        "-vn",          # 不含視訊
        "-ac", "1",     # mono
        "-ar", "16000", # 16kHz
        "-c:a", "pcm_s16le",
        str(wav_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg 音訊抽取失敗：\n{result.stderr}")


def transcribe(
    video_path: Path,
    out_srt: Path,
    model_size: str = "medium",
    device: str = "auto",
) -> list[Cue]:
    """轉錄影片音訊，產出英文 SRT 檔案，並回傳 Cue 清單。

    Args:
        video_path: 來源影片路徑。
        out_srt: 輸出 SRT 路徑（video.en.srt）。
        model_size: Whisper 模型大小（tiny/base/small/medium/large-v3）。
        device: 推論裝置（"auto"、"cpu"、"cuda"）。

    Returns:
        英文 Cue 清單。
    """
    from faster_whisper import WhisperModel

    # 解析 device
    if device == "auto":
        try:
            import torch
            resolved_device = "cuda" if torch.cuda.is_available() else "cpu"
        except ImportError:
            resolved_device = "cpu"
    else:
        resolved_device = device

    compute_type = "float16" if resolved_device == "cuda" else "int8"

    print(f"  載入 Whisper 模型：{model_size} / {resolved_device} / {compute_type}")
    model = WhisperModel(model_size, device=resolved_device, compute_type=compute_type)

    # 抽取音訊到暫存檔
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = Path(tmp.name)

    try:
        print(f"  抽取音訊：{video_path.name} → {wav_path.name}")
        extract_audio(video_path, wav_path)

        print("  開始轉錄（language=en, vad_filter=True）…")
        segments, info = model.transcribe(
            str(wav_path),
            language="en",
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500),
            beam_size=5,
        )

        cues: list[Cue] = []
        for i, seg in enumerate(segments, start=1):
            start_tc = format_timecode(seg.start)
            end_tc = format_timecode(seg.end)
            text = seg.text.strip()
            if not text:
                continue
            cues.append(Cue(index=i, start=start_tc, end=end_tc, text=text))

        # 重新編號（跳過空 segment 後可能不連續）
        for new_idx, cue in enumerate(cues, start=1):
            cue.index = new_idx

        write_srt(cues, out_srt)
        print(f"  轉錄完成：{len(cues)} 條字幕，時長 {info.duration:.1f} 秒")
        return cues

    finally:
        wav_path.unlink(missing_ok=True)
