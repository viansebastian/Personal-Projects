### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 1 Lab  -- 1:05:49

# Write a Python script that prompts the user to enter their name and password. 
# Use exception handling to validate the username is in alphabet and the password is alphanumeric

#username block
try: 
    name = input("enter username: ")
    assert name.isalpha() #assert = to check if a condition is T or F 
    
except: 
    raise ValueError ("did not input correct username or password")

else: 
    print("username: " + name)
    
finally: 
    print("thanks! \n")

#password block 
try: 
    password = input("enter pass: ")
    assert password.isalnum()
    
except: 
    raise ValueError ("did not input correct username or password")

else: 
    print("pass: " + password)
    
finally: 
    print("thanks! \n")
