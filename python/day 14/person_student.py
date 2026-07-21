class person:
    def name(self,name):
        self.name=name
        print(f"name is {self.name} ")

class student(person):
    def details(self,name,age):
        super().name
        self.age=age
        print(f"name is {name} and {self.age} years old ")

s1=student()
s2=student()
s3=student()
s1.details("yeshwanth",19)
s2.details("ramu",19)
s3.details("ragavi",18)

