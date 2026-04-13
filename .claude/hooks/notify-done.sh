#!/bin/bash
# Hook: 任務完成 Windows 氣球通知
# 事件: Stop

[ -n "$CLAUDE_SUBPROCESS" ] && exit 0

TEMP_MSG_FILE="C:\\Users\\User\\AppData\\Local\\Temp\\claude_balloon_msg.txt"
TEMP_MSG_FILE_UNIX="/c/Users/User/AppData/Local/Temp/claude_balloon_msg.txt"

# 從 stdin 取得 hook 輸入，由 Python 一次完成：讀 session_id、查 history.jsonl、寫暫存檔
cat | python3 - "$USERPROFILE/.claude/history.jsonl" "$TEMP_MSG_FILE_UNIX" << 'PYEOF'
import json, sys, os

history_file = sys.argv[1]
output_file = sys.argv[2]
default_msg = "任務完成"

try:
    hook_input = json.load(sys.stdin)
    session_id = hook_input.get("session_id", "")
except:
    session_id = ""

msg = default_msg

if session_id:
    try:
        with open(history_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
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

# 直接用 Python 寫檔，避免 bash 編碼問題
with open(output_file, "w", encoding="utf-8") as f:
    f.write(msg)
PYEOF

powershell.exe -NoProfile -NonInteractive -Command "
Add-Type -AssemblyName System.Windows.Forms
\$notify = New-Object System.Windows.Forms.NotifyIcon
\$notify.Icon = [System.Drawing.SystemIcons]::Information
\$notify.Visible = \$true
\$msg = (Get-Content '$TEMP_MSG_FILE' -Encoding UTF8 -Raw).Trim()
\$notify.ShowBalloonTip(8000, 'Claude Code', \$msg, [System.Windows.Forms.ToolTipIcon]::Info)
Start-Sleep -Seconds 9
\$notify.Dispose()
" &
