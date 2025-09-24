#93.Create a custom exception
class InvalidAgeError(Exception):
    def __init__(self,age,message="age must be between 0 and 120"):
        self.age=age
        self.message=message
        super().__init__(self.message)
def validateAge(age):
    if age<0 or age>120:
        raise InvalidAgeError(age)
    print('Valid age:',age)
try:
    age=int(input('Enter the age you want:'))
    validateAge(age)
except InvalidAgeError as e:
    print(f"InvalidAgeError:{e}")
except ValueError:
    print('please enter a numeric value')
