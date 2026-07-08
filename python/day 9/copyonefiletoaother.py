with open ("student.txt","r") as source:
    data=source.read()

with open ("studentnew.txt","w") as destination:
    destination.write(data)

with open ("studentnew.txt","r") as destination:
    file=destination.read()
    print(file)

