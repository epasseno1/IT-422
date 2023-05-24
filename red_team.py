from pymetasploit3 import *
from pymetasploit3.msfrpc import *


client = MsfRpcClient(host='127.0.0.1', port=55552, username='msf', password='OIVBfGV9' )
exploits = client.modules.exploits

def find_exploit(tm_OS, query):
    """Function that will find exploits using the os and exploit type passed to it"""
    xploit_list = []
    for item in exploits:
        if query in item and tm_OS in item:
            xploit_list.append(item)
        else:
            continue
    return(xploit_list)


OS_type = input("what OS do you want an exploit for ")
search  = input("enter the name of the exploit you want to find \n")
current_exploit = find_exploit(OS_type.lower(), search.lower())

# print the exploit along with their index for use in selecting the exploit
counter = 0
for line in current_exploit:
    print(f"{counter}. {line}")
    counter = counter + 1

exploit_selection = input("Please enter the number belonging to the exploit you wish to use  ")

# exploit module object
loaded_exploit = current_exploit[int(exploit_selection)]



print(loaded_exploit)







