class Person: 
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def printName(self): 
        print(self.first_name, self.last_name)
        
        
p1 = Person("john", "smith")
p2 = Person("chris", "Smith")
p1.printName()
p2.printName()

class Student(Person):
    def __init__(self, Person, degree):
        super().__init__(Person.first_name, Person.last_name)
        self.degree = degree
    
    def printInfo(self):
        super().printName()
        print(f"{self.first_name} : {self.degree}")
        
s1 = Student(p1, "undergrad")
s1.printInfo()