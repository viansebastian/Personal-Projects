### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 4 -- 32:07

import os
pwd = os.getcwd()
list_directory = os.listdir(pwd)
for dir in list_directory:
    print("[+]", dir)
    

# some methods from the os module to recover information 
    # os.system()       execute shell commands
    # os.listdir(path)  returns a list with the contents of the directory passed as an argument 
    # os.walk(path)     navigates all the directories in the provided path directory and returns path
    #                   directory, names of the subdirectories, and a list of filenames in the current path 
    