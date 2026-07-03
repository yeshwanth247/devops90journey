name=input("enter the name: ")
original=name
reverse=""
for i in range(len(name)-1,-1,-1):
     
     reverse+=name[i]
    

print(reverse)
if original==reverse:
    print("it is a pallindrome")
else:
    print("it is not a pallindrome")    
