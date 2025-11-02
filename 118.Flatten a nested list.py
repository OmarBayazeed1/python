#118.Flatten a nested list
#raw = [1, [2, [3, [4, [5, [6, [7, [8, 9]]]]]]], [10, [11, [12, 13]]], 14]
raw = [1, "hello", [2, [True, [3, ["world"]]]], None]

def checking(raw):
    result=[]
    for element in raw :
        if isinstance(element,list):
            result.extend(checking(element))
        else:
            result.append(element)
    return result
print(checking(raw))
