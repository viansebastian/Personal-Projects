### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Assignment 1 -- 15:10

# Write a Python script that contains sys module, arguments, and variables to execute 
# the following tasks: 
    # a. Display the name of the script 
    # b. Display the number of arguments used in the script 
    # c. Display OS platform 
    # d. Display Python package version 
    # e. Display encoding and default encoding system 
    # f. Display environment variable path 


import sys 

# name of the script
print("script name: ", sys.argv[0])

# number of arguments
print("number of arguments: ", len(sys.argv))

# OS platform
print("OS platform: ", sys.platform)

# python version  
print("python version: ", sys.version)

# encoding default decoding system 
#print("system encoding: ", sys.getfilesystemencoding())
print("default encoding: ", sys.getdefaultencoding())

# environment variable path 
print("path environment variable: ", sys.path)

