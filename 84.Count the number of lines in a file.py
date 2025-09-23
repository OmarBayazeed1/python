#84.Count the number of lines in a file
with open('E:\\AI\\Basic\\python exercises\\some.txt','r') as file:
    line_count=sum(1 for line in file)
print(line_count)
