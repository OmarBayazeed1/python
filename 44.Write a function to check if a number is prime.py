#44.Write a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(f"10 is prime {is_prime(10)}")
print(f"3 is prime {is_prime(3)}")
print(f"7 is prime {is_prime(7)}")

