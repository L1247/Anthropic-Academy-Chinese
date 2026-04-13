"""SRT/VTT 工具：解析、雙語合併、格式轉換。"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Cue:
    index: int
    start: str   # "HH:MM:SS,mmm"
    end: str     # "HH:MM:SS,mmm"
    text: str    # 可能多行，以 \n 分隔


def parse_srt(srt_path: Path) -> List[Cue]:
    """解析 SRT 檔案，回傳 Cue 清單。"""
    content = srt_path.read_text(encoding="utf-8-sig").strip()
    blocks = re.split(r"\n\s*\n", content)
    cues: List[Cue] = []
    for block in blocks:
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        try:
            index = int(lines[0].strip())
        except ValueError:
            continue
        timecode_line = lines[1].strip()
        m = re.match(
            r"(\d{2}:\d{2}:\d{2}[,\.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,\.]\d{3})",
            timecode_line,
        )
        if not m:
            continue
        start = m.group(1).replace(".", ",")
        end = m.group(2).replace(".", ",")
        text = "\n".join(lines[2:])
        cues.append(Cue(index=index, start=start, end=end, text=text))
    return cues


def write_srt(cues: List[Cue], out_path: Path) -> None:
    """將 Cue 清單寫出為 SRT 檔案。"""
    blocks = []
    for cue in cues:
        blocks.append(f"{cue.index}\n{cue.start} --> {cue.end}\n{cue.text}")
    out_path.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


def merge_bilingual(en_cues: List[Cue], zh_texts: List[str]) -> List[Cue]:
    """將英文 cue 清單與中文翻譯合併為雙語 cue 清單（英上中下）。

    Args:
        en_cues: 英文原文 cue 清單。
        zh_texts: 與 en_cues 等長的中文翻譯文字清單（每條對應一個 cue）。

    Returns:
        雙語 Cue 清單，每條 text = "英文\\n中文"。
    """
    if len(en_cues) != len(zh_texts):
        raise ValueError(
            f"英文 cue 數 ({len(en_cues)}) 與中文翻譯數 ({len(zh_texts)}) 不符"
        )
    result: List[Cue] = []
    for cue, zh in zip(en_cues, zh_texts):
        bilingual_text = f"{cue.text}\n{zh}"
        result.append(Cue(index=cue.index, start=cue.start, end=cue.end, text=bilingual_text))
    return result


def write_vtt_from_cues(cues: List[Cue], vtt_path: Path) -> None:
    """將 Cue 清單直接寫出為 WebVTT 格式（不需中間 SRT 檔案）。"""
    lines = ["WEBVTT", ""]
    for cue in cues:
        start_vtt = cue.start.replace(",", ".")
        end_vtt = cue.end.replace(",", ".")
        lines.append(str(cue.index))
        lines.append(f"{start_vtt} --> {end_vtt}")
        lines.append(cue.text)
        lines.append("")
    vtt_path.write_text("\n".join(lines), encoding="utf-8")


def split_bilingual_cues(bi_cues: List[Cue]) -> tuple[List[Cue], List[Cue]]:
    """將雙語 cue（英文\\n中文）拆回 (en_only, zh_only) 兩組 cue。

    拆分規則：text.split("\\n", 1) → 第一行為英文，其餘為中文。
    若只有一行，英中兩組皆保留該行。

    Returns:
        (en_cues, zh_cues) 兩組 cue，與 bi_cues 等長且時間碼相同。
    """
    en_cues: List[Cue] = []
    zh_cues: List[Cue] = []
    for cue in bi_cues:
        parts = cue.text.split("\n", 1)
        en_text = parts[0].strip()
        zh_text = parts[1].strip() if len(parts) > 1 else en_text
        en_cues.append(Cue(index=cue.index, start=cue.start, end=cue.end, text=en_text))
        zh_cues.append(Cue(index=cue.index, start=cue.start, end=cue.end, text=zh_text))
    return en_cues, zh_cues


def srt_to_vtt(srt_path: Path, vtt_path: Path) -> None:
    """將 SRT 檔案轉換為 WebVTT 格式。

    轉換規則：
    - 前置 "WEBVTT\\n\\n"
    - 時間碼分隔符號 "," → "."
    - 其餘格式相同
    """
    cues = parse_srt(srt_path)
    lines = ["WEBVTT", ""]
    for cue in cues:
        start_vtt = cue.start.replace(",", ".")
        end_vtt = cue.end.replace(",", ".")
        lines.append(str(cue.index))
        lines.append(f"{start_vtt} --> {end_vtt}")
        lines.append(cue.text)
        lines.append("")
    vtt_path.write_text("\n".join(lines), encoding="utf-8")


def format_timecode(seconds: float) -> str:
    """將秒數轉換為 SRT 時間碼格式 "HH:MM:SS,mmm"。"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
