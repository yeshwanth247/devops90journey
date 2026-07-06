data=[1,0,2,4,0,1,5,3,6,5]
i=0
while i<len(data):
    j=i+1
    while j<len(data):
        if data[i]==data[j]:
            data.pop(j)
        else:
            j=j+1            
    i=i+1
print(data)            