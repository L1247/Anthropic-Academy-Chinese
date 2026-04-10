#!/bin/bash
# Hook: 敏感檔案保護
# 事件: PreToolUse（Edit | Write）
# 阻止編輯 .lock、.sqlite、.db 等敏感檔案

INPUT=$(cat)

# 嘗試從 JSON 中提取檔案路徑
FILE_PATH=$(echo "$INPUT" | grep -o '"file_path":"[^"]*"' | head -1 | sed 's/"file_path":"//;s/"//')
if [ -z "$FILE_PATH" ]; then
  FILE_PATH=$(echo "$INPUT" | grep -o '"path":"[^"]*"' | head -1 | sed 's/"path":"//;s/"//')
fi

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# 受保護的檔案模式
PATTERNS=(
  "\.env$"
  "\.env\."
  "package-lock\.json$"
  "yarn\.lock$"
  "pnpm-lock\.yaml$"
  "\.sqlite$"
  "\.sqlite3$"
  "\.db$"
)

for pattern in "${PATTERNS[@]}"; do
  if echo "$FILE_PATH" | grep -qE "$pattern"; then
    echo "🚫 阻止操作：$(basename "$FILE_PATH") 是受保護的敏感檔案"
    echo "   若確實需要編輯，請手動操作。"
    exit 2
  fi
done

exit 0
