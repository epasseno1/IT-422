import os
import platform
import shutil
import subprocess
import time
#import send2trash


def getPath():
    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"
    return root_fs


def fileObjectLocator(temp_fileN, temp_type):
    root = getPath()
    my_return = os.walk(root)

    for item in my_return:
        for filename in item[temp_type]:
            if filename == temp_fileN:
                log_zip = os.path.join(item[0], filename)
                return log_zip


def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf-8').strip()


# Generate baseline that will be used at the start of the event
baseline_file = "User_baseline.txt"
if os.path.exists(baseline_file):
    old_baseline = fileObjectLocator("User_baseline.txt", 2)
    #send2trash.send2trash(old_baseline)
else:
    print "Writing Baseline"
    net_users_output = execute_command('wmic useraccount get name')
    net_users_lines = net_users_output.splitlines()
    # Filter unwanted lines from the net users output
    baseline_lines = [line.strip() for line in net_users_lines if not line.startswith(('User accounts for', '----------', 'The command completed successfully.'))]
    with open(baseline_file, 'w') as file:
        file.write('\n'.join(baseline_lines))

print "Beginning Scan"
while True:
    # Generate the current users file
    current_users_file = 'current_users_%s.txt' % time.strftime("%Y%m%d%H%M%S")
    net_users_output = execute_command('wmic useraccount get name')
    net_users_lines = net_users_output.splitlines()
    # Filter unwanted lines from the net users output
    current_users_lines = [line.strip() for line in net_users_lines if not line.startswith(('User accounts for', '----------', 'The command completed successfully.'))]

    with open(current_users_file, 'w') as file:
        file.write('\n'.join(current_users_lines))

    # Compare current users with the baseline
    with open(baseline_file, 'r') as baseline, open(current_users_file, 'r') as current_users:
        baseline_lines = set(baseline.readlines())
        current_users_lines = set(current_users.readlines())

    new_users = current_users_lines - baseline_lines

    # Perform actions for new users not present in the baseline
    for line in new_users:
        username = line.strip()
        # Perform actions for new users (replace the following print statement with desired actions)
        print "New user detected: %s" % username
        execute_command('net user %s /delete' % username)

    # Wait for 15 seconds before the next iteration
    print "The next scan will occur in 15 seconds"
    time.sleep(15)