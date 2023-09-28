### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 9 -- 1:05:21

# subprocess module : invoke and communicate with Python processes, send data input, and receive output info 
# - best used in Linux or with C-Compiler 
# - use to execute and communicate with OS commands or start programs 
# - call() to invoke a process 
# - popen() to start new process that runs specific comand 
# - terminate() to terminate the running command 

# exp 8 : ping www.google.com using Popen()

import subprocess
import sys

command_ping = '/bin/ping'
ping_parameter = '-c 1'
domain = "www.google.com"
p = subprocess.Popen([command_ping, ping_parameter, domain], shell=False, 
stderr=subprocess.PIPE)
out = p.stderr.read(1)
sys.stdout.write(str(out.decode('utf-8')))
sys.stdout.flush()