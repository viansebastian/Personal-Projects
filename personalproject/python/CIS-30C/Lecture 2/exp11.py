### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 11 -- 1:22:06

# ex 11: count characters in file 

try: 
    countlines = countchars = 0 
    file = open('newfile.txt', 'r')
    lines = file.readlines()
    for line in lines: 
        countlines += 1
        for char in line: 
            countchars += 1
    file.close()
    print("charas in file: ", countchars)
    print("lines in file: ", countlines)
except IOError as e: 
    print("I/O ERROR OCCURED", str(e))