from random import randint

class bankAccount:
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = 987654321
        self.balance = float(0)
        self.interest = float(0)

    def deposit(self):
        amount = float(input("How much would you like to deposit today? "))
        self.balance += amount
        print(f"Amount Deposited: ${amount}\n")

    def withdraw(self):
        amount = float(input("How much would you like to withdraw today? "))
        atm_fee = 4.95
        if self.balance >= amount:
            self.balance -= amount
            self.balance -= atm_fee
            print(f"Amount Withdrawn: ${amount}")
            print(f"An ATM fee of ${atm_fee} has been deducted from your account")
        else:
            self.balance -= 10.0
            print(f"The amount you have entered exceeds your available balance. Your account has been charged a $10 fee.\n")

    def get_balance(self):
        print(f"\nYour current account balance is: {self.balance}\n")
        return self.balance

    def add_interest(self):
        self.interest = self.balance * 0.00083
        self.balance += self.interest
        print(f"\nMonthly has been earned and added to your account balance.\n Interest Earned: ${self.interest}")
        return self.interest
    def print_receipt(self):
        print(self.full_name)
        print(f"Account No.: {self.account_number}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Current Balance: {self.balance}")
        print(f"Interest Earned: {self.interest}")


account1 = bankAccount("Nolan Ngo", randint(10000000,99999999))
account2 = bankAccount("Edison Li", randint(10000000,99999999))
account3 = bankAccount("Sergio Rodriguez", randint(10000000,99999999))
account4 = bankAccount("Iggi Jimenez", randint(10000000,99999999))

#These are interactions with account2, deposit, interest earned, and successful 
bankAccount.deposit(account1)
bankAccount.get_balance(account1)

bankAccount.add_interest(account1)

bankAccount.withdraw(account1)
bankAccount.get_balance(account1)

bankAccount.print_receipt(account1)

#These are interactions with account2. Overdraft will be demo'ed.
bankAccount.deposit(account2)
bankAccount.get_balance(account2)

bankAccount.add_interest(account2)

bankAccount.withdraw(account2)
bankAccount.get_balance(account2)

bankAccount.print_receipt(account2)