str=input("enter the string: ")
new_str=str
data=""
for i in range(len(str)):
    for j in range(len(str)):
        if str[i]==str[j]:
            data=data + "str[i]"
print(data)