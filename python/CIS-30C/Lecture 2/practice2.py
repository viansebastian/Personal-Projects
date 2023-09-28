### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Assignment 2 -- 43:00 

# write a Python script that contains os module to execute the following tasks: 
    # a. Display current directory 
    # b. Crate a list of files and subdirctories using os.list(), then display a list of files and subfdirectories
    #    in the current working directory
    # c. Use os.walk() and os.path() to list and display the files and subdirectories in the current working directory 
    # d. Use os.walk() and os.path() to list and display the file name and extension in the current working directory
    
import os

# display current dir 
current_dir = os.getcwd() #cwd = current working directory
print(current_dir)
print()

# make list of directories, and display
directory_list = os.listdir(current_dir) 
for directory in directory_list:
    print('[+]' , directory)
    print()
    
# list and display files and folders in cwd with os.walk() and os.path()
for root, directories, files in os.walk(".", topdown=False):
    for file_entry in files: 
        print('[+]' , os.path.join(root, file_entry))
    
    for dir in directories: 
        print('[+++]', dir)
print()

# 
import os
from collections import Counter
counts = Counter()

for currentdir, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension] += 1
        
for extension, count in counts.items():
    print(f"{extension:8}{count}")
        

    
