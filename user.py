import email


class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
link = User("Link from Zelda", "link@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(150)
guido.display_user_balance()

monty.make_deposit(250)
monty.make_deposit(575)
monty.make_withdrawal(28)
monty.make_withdrawal(49)
monty.display_user_balance()

link.make_deposit(1000)
link.make_withdrawal(323)
link.make_withdrawal(29)
link.make_withdrawal(135)
link.display_user_balance()

guido.transfer_money(link, 125)
guido.display_user_balance()
link.display_user_balance()
