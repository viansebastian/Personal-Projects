### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 1 Lab  -- 15:59 

#Write a Python script for the following tasks 
    # a.	Declare a dictionary of the user account info, which consists of username, password, email address, department
    # b.	Display the content of the dictionary 
    # c.	Use the update() to add job title/role to the dictionary 
    # d.	Display the content of the dictionary after it has been updated 
    # e.	Use len() to return and display a list of all keys in the dictionary 
    # f.	Use .keys() to return and display a list of all keys in the dictionary 
    # g.	Use .items() to return the entire list of items in a dictionary 
    # h.	Use .items() and for-loop to display key and values in the dictionary. Note: this task cannot be the same as 8B


user_account = {
    "username" : "techSAVVY875",
    "password" : "christmas123",
    "email" : "techsavvy123@mail.com",
    "department" : "IT"    
}

#display content 
print(user_account)
print()

#update() and display 
user_account.update({"job " : "software engineer"})
print(user_account)
print()

#len()
print(len(user_account))
print()

#keys()
print(user_account.keys())
print()

#items()
print(user_account.items())
print()

#items() & for-loop 
for i,j in user_account.items():
    print(i, "-", j)
    
