data=(1,2,3,1,4,5,2,8,4,1,2,6)
count=0
for i in range(len(data)):
    count=0
    for j in range(len(data)):
        if data[i]==data[j] and i!=j:

            count+=1

    print(f"the occurence of {data[i]} elements is :",count+1)            

