#101.Create a class with attributes and methods
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
myStudent=Student('omar',23)
print(f"student name: {myStudent.name}")
print(f"student age: {myStudent.age}")

myStudent.set_name('ali')
myStudent.set_age(50)
print(f"student name: {myStudent.get_name()}")
print(f"student age: {myStudent.get_age()}")
