class bankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

account1 = bankAccount("Nolan Ngo", 123456789, 7654321, 0)

print(account1.full_name)
print(account1.account_number)
print(account1.routing_number)
print(account1.balance)