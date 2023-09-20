### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Assignment 3 -- 1:00:25

# write a Python script that contains platform module to execute the following tasks: 
    # a. Display the current system OS info 
    # b. Use control statements to display appropriate commands to find IP address info in 
    #    different platforms(ipconfig -- Windows, ip addr -- Linux, ipconfig getifaddr en1 --macOS)
    # c. Display the Python implementation and version using python_implementation() and pyton_version_tuple()
     
import platform
from platform import python_implementation, python_version_tuple

# current system OS information
operating_system = platform.system()
print(operating_system)

# find IP address info 
if (operating_system == "Windows"):
    net_command = "ipconfig"
elif (operating_system == "Linux"):
    net_command = "ip addr"
else:
    net_command = "ipconfig getifaddr en1"
(net_command)


# python implementation 
print(python_implementation)
for attribute in python_version_tuple():
    print(attribute)

