#23.Compare two numbers and print the larger one
number=int(input('Enter an integer:'))
anotherNumber=int(input('Enter another integer:'))
if number>anotherNumber:
    print(number)
elif number<anotherNumber:
    print(anotherNumber)
else:
    print('Equal',f"{number} = {anotherNumber}")
