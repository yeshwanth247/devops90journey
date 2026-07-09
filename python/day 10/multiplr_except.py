try:
    num1=int(input("enter the num1: "))
    num2=int(input("enter the num2: "))
    print(num1/num2)
except ZeroDivisionError:
    print("number cannot be divided byt zero")
except ValueError:
    print("invalid input")
finally:
    print("program ended!!!!!")

