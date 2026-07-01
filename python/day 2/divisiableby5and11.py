num=int(input("enter the number: "))

if num%5==0 and num%11==0:
    print("number is divisible by 5 and 11")
elif num%5==0:
    print("number is divisible by 5 only")
elif num%11==0:
    print("number is divisible by 11 only")
else: 
    print("number is not divisible by any of 5 and 11")            