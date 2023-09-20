### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 2 Lecture Example 8 -- 58:08

# python_implementation() : returns a string with the Python implementatin 
# python_version_tuple() : returns a three-element tuple filled with information related to minor 
# and major versions, and patch level numbers

#ex 8: Display Python implementation and version

from platform import python_implementation, python_version_tuple

print(python_implementation)
for attribute in python_version_tuple():
    print(attribute)
    