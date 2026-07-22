str=input("enter the string: ")

for i in range(len(str)):
    count=0

    for j in range(len(str)):
        if str[i]==str[j]:
            count+=1
    print(f"the occurance {str[i]} in the str is: {count} ")       
