#92.Handle invalid input using try-except
try:
    name=int(input('Enter a number:'))
    print(name)
except ValueError:
    print('invalid input')
