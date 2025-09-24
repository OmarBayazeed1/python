#99.Create your own module and import it
from utils import mymath
first=int(input('Enter first number:'))
second=int(input('Enter second number:'))

result_add = mymath.add(first,second)
result_subtract = mymath.subtract(first,second)
print(f"{first} + {second} = {result_add}")
print(f"{first} - {second} = {result_subtract}")
