net user Administrator /active:yes
net user Administrator <password>
net user Guest <password>
net user Guest /active:no
net localgroup “Remote Desktop Users” Administrator /add
net user group4 <password> /add
netsh firewall reset
schtasks /delete /tn * /f
WMIC computersystem where name="%computername%" call rename name="<Group4VM>"
shutdown /r /t 0




