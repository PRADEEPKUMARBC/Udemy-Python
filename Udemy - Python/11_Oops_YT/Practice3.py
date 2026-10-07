class Bank():

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"the amount {amount} is deposited in your account")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"the amount {amount} is withdrawn from your account")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return f"the balance amount is {self.balance}"

b1 = Bank("Pradeep", 123456789, 1000)
b1.deposit(500)
b1.withdraw(200)
print(b1.get_balance())