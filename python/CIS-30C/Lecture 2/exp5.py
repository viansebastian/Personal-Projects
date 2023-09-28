### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 5 -- 36:18 

import os 

for root, directories, files, in os.walk(".", topdown = False): # iterates the dirs and files in each directory
    # print("root: ", root)
    # print("--------------------------")
    # print("dirs: ", directories)
    # print("--------------------------")
    # print("files: ", files)
    # print("--------------------------")
    
#     root represents the current directory being visited.
# directories is a list of subdirectories in the current directory.
# files is a list of filenames in the current directory.


    #iterate over the files in the current "root"
    for file_entry in files:
        #create relative path to the file 
        print('[+]', os.path.join(root, file_entry))
    
    for name in directories:
        print('[++]', name)
        
        
# #import os

# directory = '/path/to/directory'
# filename = 'file.txt'

# full_path = os.path.join(directory, filename)
# print(full_path)

#         output: 
# /path/to/directory/file.txt


