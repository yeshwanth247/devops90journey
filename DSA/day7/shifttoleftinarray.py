arr=[1,2,3,4,5,6]
new=arr[0]
for i in range(1):
    arr.pop(0)
    arr.append(new)

print(arr)