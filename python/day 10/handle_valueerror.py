try:
    num1=int(input("enter the num1: "))
    print(num1/2)
except ValueError:
    print("Invalid input....")
finally:
    print("program ended!!!!!")

