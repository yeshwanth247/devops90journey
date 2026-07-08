with open ("student.txt","r") as file:
    lines=file.readlines()
    print("the no of lines are : ",len(lines))

with open ("student.txt","r") as file:
    text=file.read()
    words=text.split()
    print("the no of words are : ",len(words))

with open ("student.txt","r") as file:
   
    line2=file.readline()

    print(line2)#wrong