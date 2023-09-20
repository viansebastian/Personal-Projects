### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 1 Lab  -- 42:32 

#declare a class 
class Employee:
    employee_count = 0
    
    #constructor 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
        Employee.employee_count += 1
        
    #methods
    def displayEmployee(self):
        print(f"Name: {self.name}, SALARY: {self.salary}")
        
def displayCount():
        print("total employee: ", Employee.employee_count)
        
emp1 = Employee("Chris", 29884)
emp2 = Employee("Iichej", 29847)

emp1.displayEmployee()
emp2.displayEmployee()
displayCount()