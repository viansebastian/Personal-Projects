### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Assignment 5 -- 1:24:12

# write a Python script that write a string, "Using Python to output text file," to a text file using 
# excpetion handling statements. 

def main(): 
    try:
        with open('ass5.txt', 'w') as file:
            file.write("Using a Python to output text file")
    except IOError as e: 
        print("Exception caught: Unable to write file", e)
    except Exception as e:
        print("Another error occured:", e)
    else: 
        print("file written successfully")

if __name__ == '__main__':
    main()
    