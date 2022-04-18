def swapList(list):
     list[0],list[-1] = list[-1],list[0]
     return list

l= [5005,2002,3003,4004,1001]

print("The list before swapping: ",l)
print("The swapped list is : ",swapList(l))
