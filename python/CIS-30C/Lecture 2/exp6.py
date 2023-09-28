### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 6 -- 41:20 

# os.walk() can act as a generator function and returns as a 
#           generator obj that implements iteration protocols 
    # returns a tuple that contains current path as a directory name 
    # list of subdirectory names 
    # list of non-directory filenames 
    
#ex 6: count number of files in the current directory using os.path.splitext(filename) to return the file name and extension 

import os
from collections import Counter
counts = Counter()

for currentdir, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension] += 1
        
for extension, count in counts.items():
    print(f"{extension:8}{count}")
        

# import os

# filename = '/path/to/file.txt'

# base_name, extension = os.path.splitext(filename)
# print('Base name:', base_name)
# print('Extension:', extension)

# output: 
#     Base name: /path/to/file
# Extension: .txt

