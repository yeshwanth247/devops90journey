num1=int(input("enter the num1: "))
num2=int(input("enter the num2: "))

try:
    print(num1/num2)
except:
    print("in valid input or connot divide by 0")
finally:
    print("the program ended!!!")