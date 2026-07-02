arr=list(map(int,input("enter the elements in array: ").split()))
smallest=arr[0]

for i in range(len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]


print(smallest,"is the smallest element in the array.")
