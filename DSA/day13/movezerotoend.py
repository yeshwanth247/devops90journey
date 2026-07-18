arr=list(map(int,input("enter the elements in the array:").split()))
count=0
i=0
while i<len(arr):
    if arr[i]==0:
        arr.pop(i)
        count+=1
    else:
        i+=1    

for i in range(count):
    arr.append(0)

print(arr)