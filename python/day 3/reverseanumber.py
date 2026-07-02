n=int(input("enter the number n:"))
sum=0

while n>0:
    reverse=n%10
    sum=sum*10+reverse

print(f"the reverse of {n} is {sum}")