try:
    num1=int(input("enter the num1: "))
    print(num1/2)
except ZeroDivisionError:
    print("number cannot be divided byt zero")
finally:
    print("program ended!!!!!")

