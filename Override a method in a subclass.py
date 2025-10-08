#107.Override a method in a subclass
class Animal:
    def spark(self):
        print('an animal sparks')
class Dog(Animal):
    def spark(self):
        print('a Dog sparks')
a1=Animal()
a1.spark()
b=Dog()
b.spark()
