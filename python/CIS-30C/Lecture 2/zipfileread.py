### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Read Zipfiles -- 1:23:28

# use zipfile module to read files in zip folder
# use yield() to return file names in the zip folder 

import zipfile

def list_files_in_zip(filename):
    with zipfile.ZipFile(filename) as myZip: 
        for zipinfo in myZip.infolist():
            yield zipinfo.filename
            
for filename in list_files_in_zip("files.zip"):
    print(filename)