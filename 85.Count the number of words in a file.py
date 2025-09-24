#85.Count the number of words in a file
with open('E:\\AI\\Basic\\python exercises\\some.txt','r') as file:
    contents=file.read()
    word_count=len(contents.split())
    print(contents.split())
print(f"word counts in the file:{word_count}")
