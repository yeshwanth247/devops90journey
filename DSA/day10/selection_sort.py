arr=list(map(int,input("enter the elements in the array: ").split()))

n=len(arr)

for i in range(len(arr)-1):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            arr[j],arr[min_index]=arr[min_index],arr[j]

print("the sorted array: ",arr)
