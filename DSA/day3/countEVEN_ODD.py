arr=list(map(int,input("enter the elements in the array: ").split()))

even_count=0
odd_count=0

for i in range(len(arr)):
    if arr[i]%2==0:
        even_count+=1
    else:
        odd_count+=1

print("no.of even numbers in array:",even_count)        
print("no.of odd numbers in array:",odd_count)        
