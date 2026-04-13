#!/usr/bin/env python3
import re
from pathlib import Path

# 正確的課程名稱對應表
lessons_correct = {
    6: ("描述（Description）", "AI 能力診斷與限制"),
    7: ("深度探討二：有效提示技巧", "深度探討二：AI 與人類合作的未來"),
    8: ("辨識（Discernment）", "實踐工作場景 1：內容創作"),
    9: ("描述—辨識循環", "實踐工作場景 2：分析與決策"),
    10: ("盡責（Diligence）", "實踐工作場景 3：編碼與技術開發"),
    11: ("課程總結", "實踐工作場景 4：學習與個人成長"),
    12: ("延伸活動", "實踐工作場景 5：策劃與執行"),
}

docs_dir = Path("docs/ai-fluency")

for lesson_num in range(6, 13):
    new_title, old_title = lessons_correct[lesson_num]
    file_path = docs_dir / f"framework-nlm-{lesson_num:02d}.md"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 修正 frontmatter 中的 title
    old_frontmatter_title = f"title: 'NLM 延伸：{old_title}'"
    new_frontmatter_title = f"title: 'NLM 延伸：{new_title}'"

    if old_frontmatter_title in content:
        content = content.replace(old_frontmatter_title, new_frontmatter_title)
        print(f"✓ 修正 framework-nlm-{lesson_num:02d}.md frontmatter title")

    # 修正 H1 標題
    old_h1 = f"# 📓 第 {lesson_num:02d} 課：{old_title}"
    new_h1 = f"# 📓 第 {lesson_num:02d} 課：{new_title}"

    if old_h1 in content:
        content = content.replace(old_h1, new_h1)
        print(f"✓ 修正 framework-nlm-{lesson_num:02d}.md H1 標題")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("\n✓ 所有課程標題修正完成")
