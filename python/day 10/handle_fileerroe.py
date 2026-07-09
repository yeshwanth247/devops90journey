

try:
    file=open("student.txt","r")
except FileNotFoundError:
    print("the file didn't existed ")
finally:
    print("program ended!!")




