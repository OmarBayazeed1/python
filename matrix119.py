#119.Create a matrix and perform row-column operations
from queue_implementation import Queue 
import copy
raw=[ [1,2,3],
      [10,20,30],
      [50,100,150],
    ]
#print(raw)
#raw operations
#... Raw swapping
def raw_swapping():    
    data=raw
    temp=data[0]
    data[0]=data[2]
    data[2]=temp
    print(data)
#... Row Scaling
def raw_scaling(row_number,scaling_number):
    data=raw
    for i in range(len(data[row_number])):
        data[row_number][i]=data[row_number][i] * scaling_number
    print(data) 
#... Row Replacement
def raw_replacement(row_number,multiply_number,new_raw_number):
    data=raw
    copy_row=data[row_number][:]
    
    for i in range(len(copy_row)):
        copy_row[i]=copy_row[i] * multiply_number
    for i in range(len(data[new_raw_number])):
        data[new_raw_number][i]=data[new_raw_number][i]+copy_row[i]
    print(data)
#Column
#...Column Swapping
def column_swapping(fSwap,sSwap):
    data=copy.deepcopy(raw)
    temp1=Queue()
    temp2=Queue()
    for row_list in data:
        temp1.enqueue(row_list[fSwap])
    for row_list in data:
        temp2.enqueue(row_list[sSwap])
    for row_list_index in range(len(data)):
        data[row_list_index][fSwap]=temp2.dequeue()
    for row_list_index in range(len(data)):
        data[row_list_index][sSwap]=temp1.dequeue()
    print(data)
    

#... Column Scaling
def column_scaling(colNumber,scaleNumber):
    data=copy.deepcopy(raw)
    for i in range(len(data)):
        data[i][colNumber]=data[i][colNumber] * scaleNumber
    print(data)
#... Column Replacement
def column_replacement(column_number,multiply_number,new_column_number):
    data=copy.deepcopy(raw)
    temp=Queue()
    for row_index in range(len(data)):
        updated_element=data[row_index][column_number] * multiply_number
        temp.enqueue(updated_element)
    for row_index in range(len(data)):
        data[row_index][new_column_number]=data[row_index][new_column_number] + temp.dequeue()
    print(data)
#-------------------------

        
