#More on polymorphismm in python.
#In python we can implement polymorphism using- 
# 1. Duck Typing
# 2. Operator overloading
# 3. Method Overloading
# 4. Method Overriding

#Duck Typing- a concept in python which doesnt care about the class or type of an object, as long as the object has the methods you need.
#Exercise 4: Duck Typing with a Payment System

# Create different classes that represent payment methods (e.g., CreditCard, PayPal). 
# Each class should have a process_payment() method. 
# Then, write a function process_payment() that can accept any of these classes and call their process_payment() method without knowing the type.

class Creditcard():

    def process_payment(self, amount):
        print(f"Processing pyment of Rs.{amount} via CreditCard")


class DebitCard():

    def process_payment(self, amount):
        print(f"Processing pyment of Rs.{amount} via DebitCard")


class Upi():

    def process_payment(self, amount):
        print(f"Processing pyment of Rs.{amount} via UPI")


class Bitcoin():

    def process_payment(self, amount):
        print(f"Processing pyment of Rs.{amount} via Bitcoin")

#Function that processes any payment mode, no matter the type
def process_payment(payment_mode, amount):
    payment_mode.process_payment(amount)

#Creating objects of different payement modes
creditcard = Creditcard()
debitcard = DebitCard()
upi = Upi()
bitcoin = Bitcoin()

#Passing different payment modes' objects to the process_payment() and processing payment.
process_payment(creditcard, 26000) #calling process_payment() of CreditCard
process_payment(debitcard, 50000)
process_payment(upi, 1200)
process_payment(bitcoin, 150000)

#It will process any payment mode as long as it has the process_payment() function defined in it.
#It will call the process_payent method on the given object if it has the method python will let us call it.


#Operator Overloading- allows us to define how operators(like: +, -, *, / etc.) wil behave for our custom objects.
#used to manipulate the behaviour of operators as per our needs.

#Example- Exercise
# Consider a Point class where we want to add to points together which means adding their x and y coordinates.

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)  
        #This statement is doing the following-
        # x = self.x + other.x
        # y = self.y + other.y
        # p = Point(x, y)

    def __repr__(self): #__repr__ or represent function is used to provide an offcial str representation for recreation of object.
        return f"Point({self.x}, {self.y})"
    

    def __str__(self): #__str__ used to provide an user friendly string representaion of object.
        return f"Point at ({self.x} and {self.y})"


p1 = Point(2, 8)
p2 = Point(3, 4)
p3 = p1 + p2 #This will call __add__() internally
print(p3)
print(repr(p3))


#Method Overriding- When a subclass provides a specific implementaion for a method already defined in the superclass.
#Allows us to extend the behavior of a superclass method.

#Example of a Animal class which is a parent of two classes like lion and elephant.
#sleep() method is overrdided in both child classes as-

class WildAnimal():

    def sleep(self):
        print("The Animal is sleeping! zzzzzz! Zzzz!")

class Lion(WildAnimal):

    def sleep(self):
        print("Lion sleeps at night!")

class Elephant(WildAnimal):

    def sleep(self):
        print("Elephant sleeps during the day!")

animals = [WildAnimal(), Lion(), Elephant()] #list of objects of WildAnimal(), Lion() and Elephant() classes.

for animal in animals:  #calling sleep() for object of every class- sleep() of the object's class will be called, no mattery the inheritance.
    animal.sleep()


#Method Overloading- Python doesnt supports method overloading traditionally. As in python a method can only be defined once.
#Overloading of methods simply means to have same names but different signatures(parameters(number and type)).
#But we can workaround to implement it by checkcing the type or number of arguments passed to the function.

class Calc():

    #Overlaoding a sum() function to make it work for upto 3 arguments, by checking number of arguments.
    def sum(self, a = None, b = None, c = None):
       
        s = 0

        if a != None and b != None and c != None:  #will work if 3 arguments are passed 
            s = a + b +c

        elif a != None and b != None:   #will work if 2 arguments are passed
            s = a + b

        else:   #will work if only one argument is passed
            s = a

        return s
        

c1 = Calc()

#calling sum() for different number of arguments
print(c1.sum(5, 10, 20))    #for 3 args
print(c1.sum(5, 10))        #for 2 args
print(c1.sum(5))            #for 1 arg
print(c1.sum())             #for no arg
