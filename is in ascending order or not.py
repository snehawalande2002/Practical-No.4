firstlist = [10,5,2,6,9]

print("The gives list is ", firstlist)
flag =0
secondlist = firstlist[:]

secondlist.sort()


if firstlist == secondlist:
     flag =1

if (flag):
    print("The given list is in ascending order")
else:
    print("The given list is not in ascending order")