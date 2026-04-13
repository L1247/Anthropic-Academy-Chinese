#!/usr/bin/env python3
"""影片自動字幕產生 CLI 主腳本。

用法：
  # 批次處理所有 exports 目錄下的影片
  python generate_subtitles.py

  # 指定單一影片
  python generate_subtitles.py --input ../../notebooklm-exports/4ds-ai-fluency/video.mp4

  # 強制重跑（覆寫已有字幕）
  python generate_subtitles.py --force

  # 只產英文字幕（跳過翻譯）
  python generate_subtitles.py --skip-translate

  # 指定模型大小
  python generate_subtitles.py --model large-v3
"""

from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

# ── 路徑設定 ──────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
EXPORTS_DIR = SCRIPT_DIR.parent.parent / "notebooklm-exports"


# ── 資料結構 ──────────────────────────────────────────────────────────────────

@dataclass
class JobResult:
    video: Path
    status: str          # "success" | "skipped" | "failed"
    message: str = ""
    elapsed: float = 0.0
    cue_count: int = 0


# ── 主邏輯 ────────────────────────────────────────────────────────────────────

def collect_videos(input_path: Optional[Path], force: bool) -> List[Path]:
    """收集需要處理的影片清單。"""
    if input_path is not None:
        # --input 可以是單一 mp4 或含 video.mp4 的目錄
        if input_path.is_dir():
            candidate = input_path / "video.mp4"
            if not candidate.exists():
                print(f"[錯誤] 目錄中找不到 video.mp4：{input_path}")
                sys.exit(1)
            input_path = candidate
        if not input_path.exists():
            print(f"[錯誤] 找不到影片：{input_path}")
            sys.exit(1)
        return [input_path]

    # 批次掃描
    videos = sorted(EXPORTS_DIR.glob("*/video.mp4"))
    if not videos:
        print(f"[警告] 在 {EXPORTS_DIR} 找不到任何 video.mp4")
        return []

    if not force:
        # 過濾：三份 VTT 都已存在才跳過
        remaining = []
        for v in videos:
            bi_vtt  = v.parent / "video.zh-Hant.vtt"
            zh_vtt  = v.parent / "video.zh-Hant-only.vtt"
            en_vtt2 = v.parent / "video.en.vtt"
            if bi_vtt.exists() and zh_vtt.exists() and en_vtt2.exists():
                print(f"  [跳過] {v.parent.name}（三份 VTT 均已存在）")
            else:
                remaining.append(v)
        return remaining

    return videos


def process_video(
    video: Path,
    model_size: str,
    device: str,
    skip_translate: bool,
    force: bool,
) -> JobResult:
    """處理單支影片，回傳結果。"""
    import transcribe as tr
    import translate as tl

    en_srt = video.parent / "video.en.srt"
    bi_srt = video.parent / "video.zh-Hant.srt"
    bi_vtt = video.parent / "video.zh-Hant.vtt"       # 雙語（英上中下）
    zh_vtt = video.parent / "video.zh-Hant-only.vtt"  # 純繁中
    en_vtt = video.parent / "video.en.vtt"            # 純英文

    t_start = time.time()

    try:
        # ── 轉錄 ──────────────────────────────────────────────────────────────
        if en_srt.exists() and not force:
            print(f"  [快取] 已有英文 SRT，跳過轉錄")
            from srt_utils import parse_srt
            en_cues = parse_srt(en_srt)
        else:
            print(f"  [轉錄] {video.name}")
            en_cues = tr.transcribe(
                video_path=video,
                out_srt=en_srt,
                model_size=model_size,
                device=device,
            )

        # ── 翻譯 ──────────────────────────────────────────────────────────────
        if skip_translate:
            # 只產英文 VTT
            from srt_utils import srt_to_vtt
            en_vtt = video.parent / "video.en.vtt"
            srt_to_vtt(en_srt, en_vtt)
            print(f"  [跳過翻譯] 已產出英文 VTT：{en_vtt.name}")
            elapsed = time.time() - t_start
            return JobResult(
                video=video,
                status="success",
                message="英文 SRT + VTT",
                elapsed=elapsed,
                cue_count=len(en_cues),
            )

        print(f"  [翻譯] 呼叫 Claude API…")
        tl.translate_srt(
            en_srt=en_srt,
            out_srt=bi_srt,
            out_vtt=bi_vtt,
            out_zh_vtt=zh_vtt,
            out_en_vtt=en_vtt,
        )

        elapsed = time.time() - t_start
        return JobResult(
            video=video,
            status="success",
            message="英文 SRT + 雙語 SRT + 三份 VTT",
            elapsed=elapsed,
            cue_count=len(en_cues),
        )

    except Exception as e:
        elapsed = time.time() - t_start
        return JobResult(
            video=video,
            status="failed",
            message=str(e),
            elapsed=elapsed,
        )


def print_summary(results: List[JobResult]) -> None:
    """印出整體摘要表。"""
    print("\n" + "=" * 60)
    print("  處理摘要")
    print("=" * 60)
    success = [r for r in results if r.status == "success"]
    failed = [r for r in results if r.status == "failed"]
    skipped = [r for r in results if r.status == "skipped"]

    for r in results:
        icon = {"success": "✓", "failed": "✗", "skipped": "–"}.get(r.status, "?")
        elapsed_str = f"{r.elapsed:.1f}s" if r.elapsed else ""
        cue_str = f"{r.cue_count} cues" if r.cue_count else ""
        detail = " | ".join(filter(None, [cue_str, elapsed_str, r.message if r.status == "failed" else ""]))
        print(f"  {icon} {r.video.parent.name:<30} {detail}")

    print("=" * 60)
    print(f"  成功：{len(success)}  |  失敗：{len(failed)}  |  跳過：{len(skipped)}")
    print("=" * 60)

    if failed:
        sys.exit(1)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="自動為 notebooklm-exports 中的影片產生雙語字幕（SRT + VTT）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input", "-i",
        type=Path,
        default=None,
        help="指定單一影片路徑（mp4 或含 video.mp4 的目錄），省略則批次掃描 exports 目錄",
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="強制重跑，覆寫已有的字幕檔",
    )
    parser.add_argument(
        "--model", "-m",
        default="medium",
        choices=["tiny", "base", "small", "medium", "large-v2", "large-v3"],
        help="Whisper 模型大小（預設：medium）",
    )
    parser.add_argument(
        "--device", "-d",
        default="auto",
        choices=["auto", "cpu", "cuda"],
        help="推論裝置（預設：auto）",
    )
    parser.add_argument(
        "--skip-translate",
        action="store_true",
        help="跳過 Claude API 翻譯，只產出英文 SRT/VTT",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  影片字幕產生器")
    print(f"  模型：{args.model}  裝置：{args.device}  翻譯：{'否' if args.skip_translate else '是（Claude API）'}")
    print("=" * 60)

    videos = collect_videos(args.input, args.force)
    if not videos:
        print("沒有需要處理的影片。")
        return

    print(f"\n共找到 {len(videos)} 支影片需要處理：")
    for v in videos:
        print(f"  • {v.parent.name}/{v.name}")
    print()

    results: List[JobResult] = []
    for video in videos:
        print(f"\n▶ 處理：{video.parent.name}")
        result = process_video(
            video=video,
            model_size=args.model,
            device=args.device,
            skip_translate=args.skip_translate,
            force=args.force,
        )
        results.append(result)
        if result.status == "failed":
            print(f"  [錯誤] {result.message}")

    print_summary(results)


if __name__ == "__main__":
    main()
