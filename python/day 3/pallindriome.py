n=int(input("enter the number n:"))
original=n
sum=0
for i in range (0,n):
    if n>0:
     reverse=n%10
     sum=sum*10+reverse
     n=n//10

print(sum)
if sum==original: print(f"{original} is a pallindrome number")
else: print(f"{original} is not a pallindrome number")


