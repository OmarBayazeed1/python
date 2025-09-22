#22.Determine if a number is even or odd
number=int(input('Enter a number:'))
condition=number %2
if condition==0:
    print('Even')
else:
    print('Odd')
