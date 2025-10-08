#102.Instantiate multiple objects from the same class
class Person:
    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
    def get_name(self):
        return name
    def get_age(self):
        return age
    def get_work(self):
        return work

    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_work(self,work):
        self.work=work
    def print_details(self):
        print('------')
        print(self.name)
        print(self.age)
        print(self.work)
        print('------')
omar=Person('omar',23,True)
ali=Person('ali',20,False)
omar.print_details()
ali.print_details()
    
