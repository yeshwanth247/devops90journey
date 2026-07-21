data=input("enter the string : ")
original=data
duplicate=""

for i in range(len(data)-1,-1,-1):
    duplicate=duplicate+data[i]

if original==duplicate:
    print("the givein string is pallindrome!!!")
else:
    print("the given string is not a pallindrome!!!")





