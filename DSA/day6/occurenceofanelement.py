#arr=list(map(int,input("enter the elements in the array: ").split()))
#count=0
#for i in range(len(arr)):
 #   for j in range(len(arr)):
  #      if arr[i]==arr[j] and i!=j:
   #         count+=1

#print("the occurance of a element is " ,count)
arr = list(map(int, input("Enter the elements: ").split()))

for i in range(len(arr)):
    count = 1

    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            count += 1

    duplicate = False
    for k in range(i):
        if arr[i] == arr[k]:
            duplicate = True
            break

    if not duplicate:
        print(arr[i], "occurs", count, "time(s)")
