class shape:
    def color(self):
        print("red")
class rectangle(shape):
    def area(self,length,breath):
        self.length=length
        self.breath=breath

        area=self.length*self.breath
        print("area is ",area)

r1=rectangle()
r1.area(10,2)



