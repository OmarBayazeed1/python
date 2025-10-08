#108.Use super() to call a parent method
class Perosn:
    def print_msg(self):
        print('hello from person')
class Student(Perosn):
    def print_msg(self):
        super().print_msg()
s1=Student()
s1.print_msg()
