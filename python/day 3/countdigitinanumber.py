n=int(input("enter the numbber: "))


digit=0
for i in range (0,n):
    if n>0 :

        digit+=1
        quotient=n//10
        n=quotient

print(f"the number of digits are {digit}")    

