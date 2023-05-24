from pymetasploit3 import *
from pymetasploit3.msfrpc import *
from pymetasploit3.msfconsole import MsfRpcConsole

# Create the RPC session
client = MsfRpcClient(host='127.0.0.1', port=55552, username='msf', password='OIVBfGV9' )

# launch the scanner module
console = MsfRpcConsole(client)


scanners = ['auxiliary/scanner/smb/smb_ms08_067','auxiliary/scanner/http/ms10_059_webdav','auxiliary/scanner/http/ms09_050_asp','auxiliary/scanner/dcerpc/endpoint_mapper','auxiliary/scanner/upnp/aadp_msearch']



def show_exploits(tmp_scanners):
    counter = 0
    for line in tmp_scanners:
        print(f"{counter}. {line}")
        counter = counter + 1

def scan_host(tmp_scanner):
    # gather the host information that will be used with scan
    current_target = input("Please enter the IP of the target machine ")
    for item in tmp_scanner:
        try:
            result = client.modules.use('auxiliary', item)
            result['RHOSTS'] = current_target
            result.execute()
        except:
            print("there was something that did not work")

def print_scanner_info(tmp_scanner):
    show_exploits(tmp_scanner)
    selected_scanner = int(input("select the scanner you want to know more about"))
    info_obj = tmp_scanner[selected_scanner]

    # use the input to gather the scanner module
    module = client.modules.use('auxiliary', info_obj)
    module_info = module.info()


    # print the required options
    required_options = module_info['required_options']
    for option_name, option_info in required_options.items():
        print(f'Option: {option_name}')
        print(f"Description: {option_info['description']}")
        print(f"Default Value: {option_info['default']}")
        print("---")

        

program_running = ""
while program_running != "q":
    user_selection = input("Please choose an option\n1. list available exploits\n2. scan a host\n3. Show scanner info ")
    if user_selection == "1":
        show_exploits(scanners)
    elif user_selection == "2":
        scan_host(scanners)
    elif user_selection =="3":
        print_scanner_info(scanners)
    program_running = input("q to quit, or enter to continue \n")




















# exploits = client.modules.exploits

# def find_exploit(tm_OS, query):
#     """Function that will find exploits using the os and exploit type passed to it"""
#     xploit_list = []
#     for item in exploits:
#         if query in item and tm_OS in item:
#             xploit_list.append(item)
#         else:
#             continue
#     return(xploit_list)


# OS_type = input("Which platform do you want an exploit for *press enter for all platforms* ")
# search  = input("Enter the vulnerability you wish to exploit *press enter for all* ")
# current_exploit = find_exploit(OS_type.lower(), search.lower())
# current_target = input("Please enter the IP of the target machine ")


# # print the exploit along with their index for use in selecting the exploit
# counter = 0
# for line in current_exploit:
#     print(f"{counter}. {line}")
#     counter = counter + 1


# exploit_selection = input("Please enter the number belonging to the exploit you wish to use  ")

# # exploit module object
# loaded_exploit = current_exploit[int(exploit_selection)]
# try:
#     exploit = client.modules.use('exploit', loaded_exploit)
#     print("The payload has been loaded")
# except:
#     print("something went wrong")


# exploit.target = current_target
# exploit.targetpayloads()
