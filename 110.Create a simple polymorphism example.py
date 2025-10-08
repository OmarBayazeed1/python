#110.Create a simple polymorphism example
#--------------------
#using inhertence and method override
class Animal:
    def speak(self):
        print('animal spkeak')
class Dog(Animal):
    def speak(self):
        print('dog speak')
class Cat(Animal):
    def speak(self):
        print('cat speak')
def make_animal_speak(animal):
    animal.speak()

d1=Dog()
c1=Cat()

make_animal_speak(d1)
make_animal_speak(c1)
#---------------
#using Duck typing
class Teacher:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
people=[Teacher('mo',40),Parent('az',35),Student('uy',15)]
for one in people:
    one.get_name()
