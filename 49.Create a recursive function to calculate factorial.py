#49.Create a recursive function to calculate factorial
def theFactorial(number):
    if number==0:
        return 1
    elif number==1:
        return 1
    else:
        return number * theFactorial(number-1)
print(f"the factorial of 4 is {theFactorial(4)}")
