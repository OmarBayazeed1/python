#87.Read a file line by line
with open('E:\\AI\\Basic\\python exercises\\some.txt','r') as file:
    lines=file.readlines()
for line in lines:
    print(line.strip())
