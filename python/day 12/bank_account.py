class bank_account:
    def __init__(self,user,balance):
        self.user=user
        self.balance=balance

    def deposit(self,deposit):
        self.deposit=deposit
        self.balance=self.deposit+self.balance
        print(f"the total balance in you account is {self.balance}")

    def withdrawl(self,withdrawl):
        self.withdrawl=withdrawl
        self.balance=self.balance-self.withdrawl 
        print(f"the total balance in you account is {self.balance}")  
            
        
u1=bank_account("yeshwanth",20000)
#u1.deposit(5000)
u1.withdrawl(5000)