#37.Find the factorial of a number using a loop
number=int(input('Enter a number:'))
'''
4
4*3!
4*3*2!
4*3*2*1!
4*3*2*1
'''
result=1
for i in range(1,number+1):
    result*=i
print(result)
