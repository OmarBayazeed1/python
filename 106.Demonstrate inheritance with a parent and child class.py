#106.Demonstrate inheritance with a parent and child class
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")
a=Animal('generic animal')
b=Dog('boby')
c=Cat('mimi')

a.speak()
b.speak()
c.speak()
