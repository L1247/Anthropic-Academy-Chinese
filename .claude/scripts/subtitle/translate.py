"""Claude API 批次翻譯：英文 SRT → 雙語 SRT（英上繁中下）。"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import List

from srt_utils import Cue, merge_bilingual, parse_srt, split_bilingual_cues, write_srt, write_vtt_from_cues

BATCH_SIZE = 40  # 每批送出的 cue 數
MAX_RETRIES = 2  # 每批最多重試次數

SYSTEM_PROMPT = """\
你是一位專業字幕翻譯員，專門將英文字幕翻譯成繁體中文。

規則：
1. 逐條翻譯，保持原意。
2. 保留技術術語（如 AI、LLM、API、framework 等）不翻譯或附上慣用譯名。
3. 不要增加、合併或拆分條目。
4. 回傳格式必須是 JSON，不要有任何額外說明文字。
"""


def _translate_batch(
    client,
    items: List[dict],
    retry: int = 0,
) -> List[str]:
    """將一批 cue 送給 Claude 翻譯，回傳等長的中文文字清單。"""
    user_content = json.dumps({"items": items}, ensure_ascii=False)
    instruction = (
        "請將以下英文字幕翻譯成繁體中文。"
        "回傳格式：{\"items\": [{\"i\": <整數>, \"zh\": \"<繁中翻譯>\"},...]}，"
        "保持 i 對應，不要遺漏或新增條目。\n\n"
        + user_content
    )

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": instruction}],
    )

    raw = response.content[0].text.strip()

    # 剝除 markdown 代碼框（```json ... ``` 或 ``` ... ```）
    if raw.startswith("```"):
        lines = raw.splitlines()
        # 移除第一行（```json 或 ```）和最後一行（```）
        inner_lines = lines[1:]
        if inner_lines and inner_lines[-1].strip() == "```":
            inner_lines = inner_lines[:-1]
        raw = "\n".join(inner_lines).strip()

    # 嘗試解析 JSON
    try:
        parsed = json.loads(raw)
        translated_items = parsed["items"]
    except (json.JSONDecodeError, KeyError) as e:
        if retry < MAX_RETRIES:
            print(f"    JSON 解析失敗，重試 ({retry + 1}/{MAX_RETRIES})…")
            time.sleep(2)
            return _translate_batch(client, items, retry=retry + 1)
        raise ValueError(f"Claude 回傳無法解析的 JSON：{e}\n原始回傳：{raw[:200]}") from e

    # 建立 i → zh 對照表
    zh_map = {item["i"]: item["zh"] for item in translated_items}

    # 依序取出（順序由原始 items 決定）
    result = []
    for item in items:
        zh = zh_map.get(item["i"])
        if zh is None:
            if retry < MAX_RETRIES:
                print(f"    索引 {item['i']} 缺失，重試 ({retry + 1}/{MAX_RETRIES})…")
                time.sleep(2)
                return _translate_batch(client, items, retry=retry + 1)
            raise ValueError(f"翻譯結果缺少索引 {item['i']}")
        result.append(zh)

    return result


def translate_srt(
    en_srt: Path,
    out_srt: Path,
    out_vtt: Path | None = None,
    out_zh_vtt: Path | None = None,
    out_en_vtt: Path | None = None,
) -> List[Cue]:
    """讀取英文 SRT，呼叫 Claude API 批次翻譯，寫出雙語 SRT（和可選的 VTT）。

    Args:
        en_srt: 英文 SRT 來源路徑。
        out_srt: 雙語 SRT 輸出路徑（video.zh-Hant.srt）。
        out_vtt: 雙語 VTT 輸出路徑（若提供則一併產出）。

    Returns:
        雙語 Cue 清單。
    """
    import anthropic
    from srt_utils import srt_to_vtt

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "未設定 ANTHROPIC_API_KEY 環境變數。"
            "請執行：export ANTHROPIC_API_KEY=sk-ant-..."
        )

    client = anthropic.Anthropic(api_key=api_key)

    en_cues = parse_srt(en_srt)
    if not en_cues:
        raise ValueError(f"SRT 檔案無有效字幕：{en_srt}")

    print(f"  翻譯 {len(en_cues)} 條字幕（每批 {BATCH_SIZE} 條）…")

    all_zh: List[str] = []
    total_batches = (len(en_cues) + BATCH_SIZE - 1) // BATCH_SIZE

    for batch_idx in range(total_batches):
        start = batch_idx * BATCH_SIZE
        end = min(start + BATCH_SIZE, len(en_cues))
        batch_cues = en_cues[start:end]

        items = [{"i": cue.index, "en": cue.text} for cue in batch_cues]
        print(f"    批次 {batch_idx + 1}/{total_batches}：cue {batch_cues[0].index}–{batch_cues[-1].index}")

        zh_batch = _translate_batch(client, items)
        all_zh.extend(zh_batch)

    bilingual_cues = merge_bilingual(en_cues, all_zh)
    write_srt(bilingual_cues, out_srt)
    print(f"  雙語 SRT 已寫出：{out_srt.name}")

    if out_vtt is not None:
        srt_to_vtt(out_srt, out_vtt)
        print(f"  雙語 VTT 已寫出：{out_vtt.name}")

    # 拆出純繁中 / 純英文 VTT
    if out_zh_vtt is not None or out_en_vtt is not None:
        en_only_cues, zh_only_cues = split_bilingual_cues(bilingual_cues)
        if out_zh_vtt is not None:
            write_vtt_from_cues(zh_only_cues, out_zh_vtt)
            print(f"  純繁中 VTT 已寫出：{out_zh_vtt.name}")
        if out_en_vtt is not None:
            write_vtt_from_cues(en_only_cues, out_en_vtt)
            print(f"  純英文 VTT 已寫出：{out_en_vtt.name}")

    return bilingual_cues
