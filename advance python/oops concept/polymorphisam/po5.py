#bank
#three method
#account creation: name,account number,minimum balance
#withdraw:amount,balance
#deposit:amount1,balance1

class bank:
    bank_name="SBI"
    def account_creation(self,name,acc_no):
        self.name=name
        self.accno=acc_no
        self.min=2000
        self.balance=self.min

    def deposit(self,amount2):
        self.amount2=amount2
        self.balance=self.balance+self.amount2
        print(self.amount2,"credited from your account balance",self.balance)
        print("total balance in your account",bank.bank_name,self.accno,"is",self.balance)

    def withdraw(self,amount1):
        self.amount1=amount1
        self.balance=self.balance-self.amount1
        if(self.amount1<=self.balance):
            print(self.amount1,"rupees debted to your account balane is",self.balance,"on your account number",self.accno,)
        else:
            print("insufficient balance")


ob=bank()
ob.account_creation("jl",123)
ob.deposit(200)
ob.withdraw(250)
