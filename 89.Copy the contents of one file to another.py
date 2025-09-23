#89.Copy the contents of one file to another
# Define source and destination file names
source_file = 'E:\\AI\\Basic\\python exercises\\some.txt'
destination_file = 'E:\\AI\\Basic\\python exercises\\another.txt'
# Open source for reading and destination for writing
with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    for line in src:
        dest.write(line)
