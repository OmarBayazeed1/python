#30.Categorize age into child, teenager, adult, or senior
age=int(input('Enter age as int:'))
if age>=70:
    print('senior')
elif age>=18:
    print('adult')
elif age>=12:
    print('teenager')
else:
    print('child')
