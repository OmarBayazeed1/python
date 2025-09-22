#34.Print a multiplication table for a given number
number=int(input('Enter the number:'))
for i in range (1,11):
    print(f"{i} * {number} =",i*number)
