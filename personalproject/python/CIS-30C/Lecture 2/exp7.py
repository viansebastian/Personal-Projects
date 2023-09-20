### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 7 -- 54:04

# platform module in Python helps you determine the OS of the system 
# platform.system() : returns the type of the OS 

#ex 7: Display command depending the returned OS type 

import platform

operating_system = platform.system()
print(operating_system)

if (operating_system == "Windows"):
    ping_command = "ping -n 1 127.0.0.1"
elif (operating_system == "Linux"):
    ping_command = "ping -c 1 127.0.0.1"
else:
    ping_command = "ping -c 1 127.0.0.1"

print(ping_command)
