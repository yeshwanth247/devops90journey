try:
    with open ("studentr.txt","r") as file:
         file.write("my name is yeshwanth !")
except FileNotFoundError:
     print("fiel not found ")
except :
     print("file is in read mode")



