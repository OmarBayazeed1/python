#40.Use a while loop to guess a secret number
secret=4
while True:
    number=int(input('Enter an int between 1 and 10:'))
    if number==secret:
        print('pass')
        break
