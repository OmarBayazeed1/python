#28.Check if a number is divisible by both 3 and 5
number=int(input('enter number: '))
condition= number%3==0 and number%5==0
if condition:
    print('ok')
else:
    print('not valid')
