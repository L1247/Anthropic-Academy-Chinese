#!/bin/bash
# Hook: 任務完成 Windows 氣球通知
# 事件: Stop
# Stop hook 會從 stdin 收到 JSON：{ session_id, transcript_path, stop_hook_active }

# 若為自動 commit 子程序，跳過通知
[ -n "$CLAUDE_SUBPROCESS" ] && exit 0

# 從 stdin 取得 transcript_path
INPUT=$(cat)
TRANSCRIPT_PATH=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('transcript_path', ''))
except:
    print('')
" 2>/dev/null)

# 從 transcript JSONL 取得 Claude 最後一段回覆文字
MSG="任務完成，等待你的指示"
if [ -n "$TRANSCRIPT_PATH" ] && [ -f "$TRANSCRIPT_PATH" ]; then
    EXTRACTED=$(python3 -c "
import json, sys, re

last_text = ''
with open(sys.argv[1], encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            # 支援 {type:'assistant', message:{content:[]}} 或 {role:'assistant', content:[]}
            role = obj.get('type') or obj.get('role', '')
            content = None
            if obj.get('message') and obj['message'].get('content'):
                content = obj['message']['content']
            elif obj.get('content'):
                content = obj['content']

            if role == 'assistant' and isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get('type') == 'text':
                        text = item.get('text', '').strip()
                        # 過濾太短或純符號的文字
                        if len(text) > 15:
                            last_text = text
        except:
            pass

if last_text:
    # 移除多餘換行，截斷至 120 字
    clean = re.sub(r'[\r\n]+', ' ', last_text)
    clean = re.sub(r'\s{2,}', ' ', clean).strip()
    print(clean[:120] + ('...' if len(clean) > 120 else ''))
" "$TRANSCRIPT_PATH" 2>/dev/null)

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
