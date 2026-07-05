arr=list(map(int,input("enter the elements in the array: ").split()))
largest=arr[0]

for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]

second_largest=arr[0]
for i in range(len(arr)):
    if arr[i]>second_largest and arr[i]<largest:
        second_largest=arr[i]

print("the largest element in the array is: ",largest)
print("the second largest element in the array is: ",second_largest)

