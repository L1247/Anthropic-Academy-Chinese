#!/bin/bash
# Hook: 任務完成 Windows 氣球通知
# 事件: Stop

[ -n "$CLAUDE_SUBPROCESS" ] && exit 0

# 從 stdin 取得 session_id
INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('session_id', ''))
except:
    print('')
" 2>/dev/null)

# 從 history.jsonl 取得該 session 的第一筆 display（即 sidebar 顯示的任務名稱）
HISTORY_FILE="$USERPROFILE/.claude/history.jsonl"
MSG="任務完成"

if [ -n "$SESSION_ID" ] && [ -f "$HISTORY_FILE" ]; then
    EXTRACTED=$(python3 -c "
import json, sys

session_id = sys.argv[1]
history_file = sys.argv[2]
first_display = ''

with open(history_file, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            if obj.get('sessionId') == session_id and obj.get('display'):
                first_display = obj['display'].strip()
                break  # 取第一筆即停止
        except:
            pass

if first_display:
    # 移除換行，截斷至 50 字
    clean = first_display.replace('\n', ' ').replace('\r', '').strip()
    print(clean[:50] + ('...' if len(clean) > 50 else ''))
" "$SESSION_ID" "$HISTORY_FILE" 2>/dev/null)

    [ -n "$EXTRACTED" ] && MSG="$EXTRACTED"
fi

# 寫入暫存檔避免引號跳脫問題
echo "$MSG" > /tmp/claude_balloon_msg.txt

powershell.exe -NoProfile -NonInteractive -Command "
Add-Type -AssemblyName System.Windows.Forms
\$notify = New-Object System.Windows.Forms.NotifyIcon
\$notify.Icon = [System.Drawing.SystemIcons]::Information
\$notify.Visible = \$true
\$msg = (Get-Content 'C:\Users\User\AppData\Local\Temp\claude_balloon_msg.txt' -Encoding UTF8 -Raw).Trim()
\$notify.ShowBalloonTip(8000, 'Claude Code', \$msg, [System.Windows.Forms.ToolTipIcon]::Info)
Start-Sleep -Seconds 9
\$notify.Dispose()
" &
