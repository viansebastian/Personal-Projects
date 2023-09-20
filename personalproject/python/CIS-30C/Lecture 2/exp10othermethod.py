def main(): 
    try:
        with open('test.txt', 'w') as file:
            file.write("this is  test file ")
    except IOError as e: 
        print("Exception caught: Unable to write file", e)
    except Exception as e:
        print("Another error occured:", e)
    else: 
        print("file written successfully")

if __name__ == '__main__':
    main()