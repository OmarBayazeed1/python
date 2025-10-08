#104.Implement class vs. instance variables
class Person:
    state='person is a human'
    def __init__(self,name):
        self.name=name
    def print_details(self):
        print(self.name)
omar=Person('omar')
omar.print_details()
print(f"person state {Person.state}")
print(f"omar state {omar.state}")
omar.state='zzz'
print(f"update omar.state {omar.state}")
print(f"person state {Person.state}")
print(f"update person.state {Person.state}")
