list1 = [200,100,50,25,5]
list2 = [100,50,25,5,5]

difference =[]

result = zip(list1,list2)
for i , j in result:
    difference.append(i-j)
print(difference)