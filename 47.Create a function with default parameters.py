#47.Create a function with default parameters
def largestInList(anyList=[10,20]):
    return max(anyList)
print(f"the largest of default parameters list is {largestInList()}")
