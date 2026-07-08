with open ("student.txt","w") as file:
    file.write("\nyesh, cse, and KG Reddy ")


with open("student.txt","r") as file:
    read=file.read()
    print(read)

file=open("student.txt","a")
file.write("\nmy dream office is google")
file.close()


with open("student.txt","r") as file:
      reda=file.read()
      print(reda)


