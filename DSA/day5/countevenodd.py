arr=list(map(int,input("enter the elements in the array: ").split()))
count_even=0
count_odd=0
for i in range(len(arr)):
       if arr[i]%2==0:
              count_even+=1
       elif arr[i]%2!=0:
              count_odd+=1      

print("no.of even : ",count_even)
print("no.of odd : ",count_odd)
