#86.Replace a word in a file with another word
with open('E:\\AI\\Basic\\python exercises\\some.txt','r') as file:
    contents=file.read()
print(contents)
contents=contents.replace('is','is not')
with open('E:\\AI\\Basic\\python exercises\\some.txt','w') as file:
    contents=file.write(contents)
with open('E:\\AI\\Basic\\python exercises\\some.txt','r') as file:
    contents=file.read()
print(contents)

