#!/bin/bash
# Hook: 任務完成 Windows 氣球通知
# 事件: Stop

# 若為自動 commit 子程序，跳過通知
[ -n "$CLAUDE_SUBPROCESS" ] && exit 0

powershell.exe -NoProfile -NonInteractive -c "
Add-Type -AssemblyName System.Windows.Forms;
\$notify = New-Object System.Windows.Forms.NotifyIcon;
\$notify.Icon = [System.Drawing.SystemIcons]::Information;
\$notify.Visible = \$true;
\$notify.ShowBalloonTip(6000, 'Claude Code', '任務完成，等待你的指示 👋', [System.Windows.Forms.ToolTipIcon]::Info);
Start-Sleep -Seconds 7;
\$notify.Dispose()
" &
