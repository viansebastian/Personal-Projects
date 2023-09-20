### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 10 -- 1:14:47

# file.write(string) : 
# file.read([bufsize]) : reads up to bufsize, number of bytes from the file. size is optional, it will rad the entire fiel 
# file.readline([bufsize]) : reads one line from the file 
# file.close() : closes the and destroys the the file object 

# ex 10: open, write string to file, test.txt, and close file 

def main():
    with open('test.alana', 'w') as file: 
        file.write('alana ')
    
if __name__ == '__main__':
    main()
    
    
