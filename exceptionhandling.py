#try and except blocks:-
#Prog to print multiplication table of a num
num = input("Enter a num: ")

try: #runs when no error
    for i in range(1, 11):
        print(f"{int(num)} X {i} = {int(num) * i}")
except Exception as e: #runs if the try block catches an error
    print(e)

print("This is the end of Program!")

#Handling specific errors or exceptions
try:
    num = int(input("Enter an integer: "))
    a = [6, 2, 8]
    print(a[num])
except ValueError:
    print("The input is not an integer!")
except IndexError:
    print("Enter a valid index, the length of the list is 3.")

#Exercise1
try:
    num = int(input("Enter an integer value: "))
    print("Thanks for entering an integer value!")
except ValueError:
    print("You've entered a non integer value!")

#Exercise 2: Division Calculator with ZeroDivisionError
try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter a denominator: "))
    r = a / b
    print(f"{a}/{b} = {r}")
except ZeroDivisionError:
    print("You cannot divide by zero! Please try again.")
except ValueError:
    print("Please enter an integer value.")

#finally block
def table():

    try: 
        num = int(input("Enter a num: "))
        for i in range(1, 11):
            print(f"{int(num)} X {i} = {int(num) * i}")
    
    except:
        return "invalid input"
    
    finally:
        print("i am always executed no matter what")
    
x = table()
print(x)


#Raising custom errors/exceptions

n = int(input("Enter any value between 1 and 10: "))

if (n < 1 or n > 10):
    raise ValueError("value should be between 1 and 10")
else:
    print("Done!")

#Exercise 3: Withdrawal from Bank Account
'''Problem Statement: Create a program that simulates a bank account with a balance of 1000. 
The program should ask the user for an amount to withdraw. 
If the user tries to withdraw more money than the account balance, 
raise a ValueError with the message: "Insufficient funds. Please enter a valid amount.
" If the withdrawal is successful, deduct the amount from the balance and print the remaining balance.'''

balance = 1000

amt = int(input("Enter an amount to withdraw: "))
if amt > balance:
    raise ValueError("Insufficient funds. Please enter a valid amount")
else:
    balance -= amt
    print(f"Withdrawal Successful, Your account balance is Rs.{balance}")

#Exercise 4: Input Validation for Positive Numbers
'''Problem Statement: Write a program that asks the user for a positive number. 
If the user enters a negative number, raise a custom exception called 
ValueError with the message: "The number must be positive." 
If the user enters a valid positive number, print it.'''

num = int(input("Enter a +ve number: "))
if num < 0:
    raise ValueError("The number must be positive")
else: 
    print(num)

#Defining and raising custom exceptions

#Exercise 5: Raising Exceptions Based on Condition
'''Problem Statement: Create a program that accepts a username and password from the user. 
If the username is "admin" and the password is "1234", the program should print a success message. 
Otherwise, raise a PermissionError with the message "Invalid credentials, please try again.'''

class PermissionError(Exception):
    pass

try:
    username = input("Enter your username: ")
    passw = int(input("Enter your password: "))

    if username != "admin" or passw != 1234:
        raise PermissionError("Invalid credentials, please try again")
    else: 
        print("Login Successful")
except ValueError:
    print("Error! Password should be numeric")


