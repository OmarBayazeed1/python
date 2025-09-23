#65.Remove an element from a set
names={'omar','ali','nader'}
print(names)
#remove() take parameter and don't show and
#error if it does not found the element
names.discard('mo')

print(names)
#discard() take parameter and show 
#an error if it does not found the element
names.remove('mo')
print(names)
#does not take a parameter

names.pop()
print(names)
