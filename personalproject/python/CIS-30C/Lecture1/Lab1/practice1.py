### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 1 Lab  -- 47:09

# Write a Python script that displays network device info, such as IP address,
# and fulfill the below requirements
    # a. The program should define a class and instantiate objects to access attributes 
    # b. The class should consist of member variables, constructors, member methods and objects 
    # c. Test the program using at least 2 arguments that contain device information 


class Devices: 
    listed_devices = 0
    
    def __init__(self, name, ip_Address):
        self.name = name
        self.ip_Address = ip_Address
        Devices.listed_devices += 1
        
    def displayDevInfo(self):
        print(f"device name: {self.name}, ip address: {self.ip_Address}")


def listedDevices():
        print(f"listed devices: {Devices.listed_devices}")
    
dev1 = Devices("Navgear Switch", "213.67.125.192")
dev2 = Devices("Crimson Sat", "92.205.12.34")

dev1.displayDevInfo()
dev2.displayDevInfo()
listedDevices()
