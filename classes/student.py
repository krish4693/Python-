class Student:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
A=Student("Ananthu",20,20000)
A.display()