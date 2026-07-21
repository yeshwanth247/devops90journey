class parent:
    #def house(self):
       # print("the house is built by the parent ")

        def __init__(self):
            print("parents are the orgin")

class child(parent):
    #def phone(self):
     #super().house()
     #print("the phone belongs to the child")
     def __init__(self):
        super().__init__()
        print("child are roots")


    

c1=child()
#c1.phone()

#c1.house()




