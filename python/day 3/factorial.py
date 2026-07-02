n=int(input("enter the number of factorial:"))
factorial=1

for i in range(1,n+1):
    if n==0 or n==1:
        print("the factorial is 1")
    else:    
        factorial*=i

print(f"the factorial of{n} is {factorial}")