arr=list(map(int,input("enter the elements in the array: ").split()))

target=int(input("enter the number to find: "))

for i in range(len(arr)):
    if arr[i]==target:
        print("element found at index",i)
        break

else: print("element is not found")    

