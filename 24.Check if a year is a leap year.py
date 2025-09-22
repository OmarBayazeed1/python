'''
 A year divisible by 4 is a leap year, but years divisible by 100 are only
 leap years if they are also divisible by 400
 (e.g., 2000 was a leap year, but 1900 was not).
'''
#24.Check if a year is a leap year
year=int(input('Enter a year'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is leap year.")
    else:
        print(f"{year} is leap year.")
