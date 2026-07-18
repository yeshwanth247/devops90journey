arr=list(map(int,input("enter the elements in the array: ").split()))
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>arr[0]:
        largest=arr[i]


print("the largest elemenmt is :",largest)
second_largest=arr[0]
for i in range(len(arr)):
    if arr[i]>second_largest and arr[i]<largest:
        second_largest=arr[i]

print("the second laregest number in array is:",second_largest)
