arr=list(map(int,input("enter the elements in the array : ").split()))
arr2=[]
for i in range(len(arr)-1,-1,-1):
    #print(arr[i])
    arr2.append(arr[i])
   
print(arr2)