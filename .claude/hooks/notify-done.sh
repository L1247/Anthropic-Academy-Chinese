#!/bin/bash
# Hook: 任務完成 Windows 氣球通知
# 事件: Stop

[ -n "$CLAUDE_SUBPROCESS" ] && exit 0

TEMP_MSG_FILE_UNIX="/c/Users/User/AppData/Local/Temp/claude_balloon_msg.txt"
TEMP_MSG_FILE_WIN="C:\\Users\\User\\AppData\\Local\\Temp\\claude_balloon_msg.txt"

# 先把 stdin 存到變數，避免 heredoc 搶走 stdin
HOOK_INPUT=$(cat)

# Python 從環境變數讀 hook input，寫任務名稱到暫存檔
HOOK_INPUT="$HOOK_INPUT" \
HISTORY_FILE="$USERPROFILE/.claude/history.jsonl" \
OUTPUT_FILE="$TEMP_MSG_FILE_UNIX" \
python3 << 'PYEOF'
import json, sys, os

hook_input_str = os.environ.get("HOOK_INPUT", "")
history_file = os.environ.get("HISTORY_FILE", "")
output_file = os.environ.get("OUTPUT_FILE", "")
default_msg = "任務完成"
msg = default_msg

try:
    hook_input = json.loads(hook_input_str)
    session_id = hook_input.get("session_id", "")
except:
    session_id = ""

if session_id and history_file:
    try:
        with open(history_file, 'rb') as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    if obj.get("sessionId") == session_id and obj.get("display"):
                        display = obj["display"].replace("\n", " ").replace("\r", "").strip()
                        msg = display[:50] + ("..." if len(display) > 50 else "")
                        break
                except:
                    pass
    except:
        pass

with open(output_file, "w", encoding="utf-8") as f:
    f.write(msg)
PYEOF

powershell.exe -NoProfile -NonInteractive -Command "
Add-Type -AssemblyName System.Windows.Forms
\$notify = New-Object System.Windows.Forms.NotifyIcon
\$notify.Icon = [System.Drawing.SystemIcons]::Information
\$notify.Visible = \$true
\$msg = (Get-Content '$TEMP_MSG_FILE_WIN' -Encoding UTF8 -Raw).Trim()
\$notify.ShowBalloonTip(8000, 'Claude Code', \$msg, [System.Windows.Forms.ToolTipIcon]::Info)
Start-Sleep -Seconds 9
\$notify.Dispose()
" &
