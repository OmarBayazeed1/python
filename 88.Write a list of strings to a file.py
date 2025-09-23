#88.Write a list of strings to a file
text=['first\n','second\n','third\n']
with open('E:\\AI\\Basic\\python exercises\\some.txt','w') as file:
    file.writelines(text)
