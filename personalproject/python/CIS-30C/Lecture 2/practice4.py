### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Assignment 4 -- 1:12:32

# write a Python script to be used on a Linux system and implements subprocess module 
# to execute to ping www.youtube.com 4 times. NOTE: to test scrip, Linux system is needed 

import subprocess
import sys

command_ping = '/bin/ping'
ping_parameter = '-c 4'
domain = "www.youtube.com"
p = subprocess.Popen([command_ping, ping_parameter, domain], shell=False, 
stderr=subprocess.PIPE)
out = p.stderr.read(1)
sys.stdout.write(str(out.decode('utf-8')))
sys.stdout.flush()