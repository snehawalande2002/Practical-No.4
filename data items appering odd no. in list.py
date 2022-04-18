def fun(arr,arr_size):
    for i in range(0,arr_size):
        count = 0
        for j in range(0,arr_size):
            if arr[i] == arr[j]:
                count = count+1
            if (count % 2 != 0):
                return arr[i]

        return -1

arr =[1,2,5,1,3,1,2,5]
n = len(arr)
print(fun(arr,n))