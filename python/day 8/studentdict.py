student={
    "name":"yesh",
    "age":21,
    "branch":"cse",
    "contact":8688665356

}
print("only keys : ")
for key in student:
    print(key)

print("only values : ")
for value in student.values():
    print(value)

print("both keys ad values : ")
for key,value in student.items():
    print(key,value)
