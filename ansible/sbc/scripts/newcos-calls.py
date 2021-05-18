
#!/usr/bin/env python3
import os
import time
import subprocess
from datetime import datetime

def clean_logs():
    pass

def start_calls():
    timestamp = datetime.now()
    timestamp = str(timestamp)
    cmd = ["ps -ef | grep 'sbc_audiocodes_ssh_calls' | grep -v grep | awk '{print $2}' | xargs -r kill -9"
            ,"ansible-playbook sbc_audiocodes_ssh_calls.yaml >> log/calls_" + timestamp.split()[0] + ".log &"]
    result = [os.system(cmd[0]),os.system(cmd[1])]

    if result[1]:
        print("Error starting process!")
    else:
        print("Process started successfully! Active Calls!")

    return result[1]


result = start_calls()

print("Time: " + str(datetime.now()).split()[1].split('.')[0]) 
