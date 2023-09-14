# parent Class
class User ():
    def __init__(self,name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details(self):
        print('Persnol Details ')
        print('  ')
        print('Name ',self.name)
        print('Age ', self.age)
        print("Gender ",self.gender)
    
# child Class

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0

    def deposite(self,amount):
        self.amount= amount
        self.balance=self.balance+self.amount
        print('Account balance has been updated : $',self.balance)
    
    def withdraw(self,amount):
        self.amount=amount
        if self.amount> self.balance:
            print('Insufficient Funds : Balamce Available :$',self.balance)
        else:
            self.balance=self.balance - self.amount
            print("account Balance has been updated :$",self.balance)
    def view_balnce(self):
        self.show_details()
        print("account Balance :$",self.balance)

alex=Bank('yash',15,"m")
alex.deposite(100)