#Access Modifiers

class Bank():

    def __init__(self, owner, balance):
        self.owner = owner  #owner is a public attribute
        self.__balance = balance #__balance is a private attribute and cannot be accessed directly.
    
    #getter method for accessing balance
    def get_balance(self):
        return self.__balance
    
    #setter method for modifying balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be +ve!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else: 
            print("Invalid withdrawal amount!")

c1 = Bank("Anuvansh", 200000)
# print(c1.__balance) This will throw an error as we cannot directly access a provate attribute.
print(c1.owner) #accessing public attribute directly
#accessing and modifying private attribute using its getter and setter methods.
print(c1.get_balance())
c1.deposit(50000)
print(c1.get_balance())
c1.withdraw(25000)
print(c1.get_balance())