#90.Delete a file using Python
import os
# Specify the file name
file_to_delete = 'E:\\AI\\Basic\\python exercises\\another.txt'
# Delete the file
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f'{file_to_delete} has been deleted.')
else:
    print(f'{file_to_delete} does not exist.')
