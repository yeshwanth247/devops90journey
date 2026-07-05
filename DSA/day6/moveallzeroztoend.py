arr=list(map(int,input("enter the elements in the array: ").split()))
count_zero=0
i=0
while i<len(arr):
     if arr[i]==0:
          count_zero +=1
          arr.pop(i)
     else:
          i+=1          
         
 
         

for i in range(count_zero+1):
     arr.append(0)


print(arr)

