net user Administrator /active:yes
net user Administrator <password>
net user Guest <password>
net user Guest /active:no
net localgroup “Remote Desktop Users” "Administrator" /add
net user group4 <password> /add
schtasks /delete /tn * /f
shutdown /r /t 0




