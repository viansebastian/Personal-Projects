### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 1  -- 6:48

import sys

print("this is the name of the script: ", sys.argv[0])
print("the number of arguemnts: ", len(sys.argv))
print("the arguments are: ", str(sys.argv))

#lines under wont work as theres only one argument (Line 7)
#print("the first argument is: ", sys.argv[1]) 
#print("the second argument: ", sys.argv[2])