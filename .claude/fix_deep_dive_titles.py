#!/usr/bin/env python3
from pathlib import Path

# 修正標題 - 移除「深度探討一」和「深度探討二」
fixes = {
    3: ("什麼是生成式 AI？", "深度探討一：什麼是生成式 AI？"),
    7: ("有效提示技巧", "深度探討二：有效提示技巧"),
}

docs_dir = Path("docs/ai-fluency")

for lesson_num, (new_title, old_title) in fixes.items():
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

print("\n✓ 所有「深度探討」標籤移除完成")
