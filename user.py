import email


class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
link = User("Link from Zelda", "link@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(150).display_user_balance()

monty.make_deposit(250).make_deposit(575).make_withdrawal(28).make_withdrawal(49).display_user_balance()

link.make_deposit(1000).make_withdrawal(323).make_withdrawal(29).make_withdrawal(135).display_user_balance()

guido.transfer_money(link, 125).display_user_balance()

link.display_user_balance()
