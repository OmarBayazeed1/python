#29.Find the largest of three numbers
number1=int(input('Enter the first number:'))
number2=int(input('Enter the second number:'))
number3=int(input('Enter the third number:'))

if number1>number2:
    if number1>number3:
        print('largest is ',number1)
    else:
        print('largest is',number3)
else:
    if number2>number3:
        print('largest is',number2)
    else:
        print('largest is', number3)
