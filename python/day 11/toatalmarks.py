class total_marks:
    def __init__(self,name,maths,physics,chemistry):
        self.name=name
        self.maths=maths
        self.physics=physics
        self.chemistry=chemistry

        total=maths+physics+chemistry
        print(f"total marks obtained by {name} is :",total)

s1=total_marks("yeshwanth",92,84,62)

print(s1)