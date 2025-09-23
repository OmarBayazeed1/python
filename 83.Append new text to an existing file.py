#83.Append new text to an existing file
with open('E:\\AI\\Basic\\python exercises\\some.txt','a') as file:
    contents=file.write('\nthis text is added')
print(contents)
