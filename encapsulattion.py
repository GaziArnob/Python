class BankAccount:
    def __init__(self, name, balance, id, bank_name):
        self.__name = name # Private variable
        self.__balance = balance # Private variable
        self._id = id # Protected variable
        self.bank_name = bank_name # Public variable 



    def get_balance(self):
        return self.__balance   

acc1 = BankAccount("Arnob", 1000, 12345, "ABC Bank")

# Accessing private variables using name mangling
print(acc1._BankAccount__name)      # Arnob
print(acc1._BankAccount__balance)   # 1000

print(acc1._id)                     # 12345
print(acc1.bank_name)               # ABC Bank
print(acc1.get_balance())           # 1000