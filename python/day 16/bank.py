class bank:
    def __init__(self):
        self.__balance=40000

    def deposit(self,deposit):
        self.deposit=deposit
        self.__balance=self.__balance+self.deposit 

    def withdrawl(self,withdrawl):
        self.withdrawl=withdrawl
        self.__balance=self.__balance-self.withdrawl 

    def display_balance(self):
        return self.__balance


b=bank()
b.deposit(1000)

print(b.display_balance())

