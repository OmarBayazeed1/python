#36.Count the number of vowels in a string
name=input('Enter a name:')
result=0
for i in name:
    condition= i.lower()=='a'or i.lower()=='i' \
               or i.lower()=='e' or i.lower()=='o' \
               or i.lower()=='u'
    if condition:
        result+=1
print(result)
