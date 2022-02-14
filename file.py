class User (): 
    def __init__(self, first_name, last_name): 
        self.first_name = first_name 
        self.last_name = last_name 
        self.account_balance = 0 
    
    def make_deposit (self, amount): 
        self.account_balance += amount 

    def make_withdrawal (self, amount): 
        self.account_balance -= amount 

    def display_user_balance(self): 
        print(f"User: {self.first_name} {self.last_name} Balance: {self.account_balance}")
    
    def transfer_money(self, other_user, amount): 
        other_user = User("first_name", "last_name")
        self.account_balance -= amount 
        other_user.account_balance += amount 

zee = User("zainab", "mirza") 
elle = User("lubna", "mirza") 
sana = User("sana", "mirza")

zee.make_deposit(300)
zee.make_deposit(2500)
zee.make_deposit(2100)
zee.make_withdrawal(350)
print(zee.display_user_balance()) 

elle.make_deposit(25000)
elle.make_deposit(320)
elle.make_withdrawal(3000)
print(elle.display_user_balance())

sana.make_deposit(3100)
sana.make_withdrawal(310)
sana.make_withdrawal(400)
sana.make_withdrawal(400) 
print(sana.display_user_balance())

zee.transfer_money(sana, 500) 
print(zee.display_user_balance())
print(sana.display_user_balance())