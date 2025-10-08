#105.Create a class method and a static method
class Person:
    state='person is human'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def greeting():
        print('hello')
    @classmethod
    def interact_with_state(cls,newState):
        cls.state=newState
p1=Person('omar',23)
p1.greeting()
p1.interact_with_state('person is monkey')
print(p1.state)
print(Person.state)
