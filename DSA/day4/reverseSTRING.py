name=input("enter the name ")

for i in range(len(name)-1, -1, -1): #(l;en(name)-1(toalindex:4-1=3),stopping value,decrement)
                                         #range(start, stop, step)
    print(name[i], end="")