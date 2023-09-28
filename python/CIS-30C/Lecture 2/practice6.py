### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Assignment 6 -- 1:30:58

# refer to notes and documentaton. write a Python script that fulfills the following tasks: 
# a. create a parent folder and a child folder 
# b. zip the parent foler 
# c. use zipfile module to access the zip folder and display its content 

import os 
import zipfile

# make folder
os.mkdir("Exercise68")
print("created folder Excercise68")

# zip folder 
zf = zipfile.ZipFile("Exercise68.zip", "w")
for dirname, subdirs, files in os.walk("Exercise68"):
    zf.write(dirname)
    for filename in files: 
        zf.write(os.path.join(dirname,filename))
        
zf.close()
print(dirname)