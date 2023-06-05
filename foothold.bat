net user administrator /active:yes 

Net user administrator 

Net localgroup “Remote Desktop Users” Administrator /add 

net user group4 /add 

netsh firewall reset 

netsh firewall add allowedip 10.254.4.64 

netdom renamecomputer %COMPUTERNAME% /newname:<Group4VM> /reboot:0 
