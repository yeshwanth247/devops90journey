arr=list(map(int,input("enter the elements in the array: ").split()))
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]


target =int(input("enter the target: "))

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2 

    if arr[mid] == target:
        print("Element found at index", mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")







