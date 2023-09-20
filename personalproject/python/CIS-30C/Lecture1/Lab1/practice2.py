### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 1 Lab  -- 56:45 

# Write a Python script that uses class inheritance to display device information such as name, 
# IP adress and location. The program should fulfill the below requirements
    # a. The program should contain a parent and a child class 
    # b. The child class should inherit attributes from the parent class to add additional information abt the device, such as location


class Device: 
    def __init__(self, name, IPaddress): 
        self.name = name
        self.IPaddress = IPaddress
        print(f"Device name: {name}")
        print(f"IP address: {IPaddress}")
        
class Loc(Device):
    def __init__(self, name, IPaddress, location):
        super().__init__(name, IPaddress)
        self.location = location
        print("location:", location)
        
dev1 = Loc("Navgear Sat", "10.12.23.44", "HQ")     