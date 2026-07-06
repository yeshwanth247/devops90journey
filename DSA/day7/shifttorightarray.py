arr=[1,2,3,4,5,6]
size=len(arr)-1
new=arr.pop()

for i in range(len(arr)-1):
     if i<1:
      arr.insert(0,new)

print(arr)