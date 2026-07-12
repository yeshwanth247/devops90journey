class book:

    def __init__(self,title,author,price):
            self.title=title
            self.author=author
            self.price=price

    def display(self):
        print(f"{self.title} by -{self.author} will be price of {self.price} in dollars..") 



b1=book("'the king and maid'","ramukotel",10)
b2=book("'the gem in coal'","vishwanath",15.6)
b1.display()
b2.display()


        