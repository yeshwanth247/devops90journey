arr=list(map(int,input("enter the elements  in array: ").split()))

largest=arr[0]

for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
        


print("the largest element in the array is :",largest) 