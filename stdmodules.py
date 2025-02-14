'''Exercise 1: Using the math Module
Task: Write a Python program that:
Takes a positive integer as input from the user.
Calculates and prints:
The square root of the number.
The factorial of the number.
The sine, cosine, and tangent of the number (consider the number in radians).'''

import math

n = int(input('Enter a +ve integer: '))

print(f"Square root of {n} is {math.sqrt(n)}")
print(f"Factorial of {n} is {math.factorial(n)}")
print(f"sin({n}) = {math.sin(n)}\ncos({n}) = {math.cos(n)}\ntan({n}) = {math.tan(n)}")

'''Exercise 2: Using math module
Task: Write a Python program that:
Takes a number as input from the user.
Prints the following calculations:
-The logarithm of the number (base 10).
-The number raised to the power of 3.
-The absolute value of the number.
'''
n = int(input("Enter a number:  "))

if n > 0:
    print(f"log({n})10 is {math.log10(n)}")
else: 
    print("Logarithm is undefined for zero and negative numbers.")

print(f"{n} raise to the power 3 is {math.pow(n, 3)}")
print(f"absolute value of {n} is {abs(n)}")


'''Exercise 3: using math module
Task: Write a Python program that:
-Asks the user to input two numbers.
-Prints the following:
-The greatest common divisor (GCD) of the two numbers.
-The least common multiple (LCM) of the two numbers.'''

a = int(input("Enter a num: "))
b = int(input("Enter a num: "))

print(f"GCD of {a} and {b} is {math.gcd(a, b)}")
print(f"LCM of {a} and {b} is {abs(a * b) / math.gcd(a, b)}")

'''Financial Tracker (Using math)
Scenario: You are building a simple financial tracker for a user to keep track of their savings and expenses.

Task: Write a Python program that:

Asks the user to input their initial savings amount.
Asks the user to input monthly expenses (can be multiple inputs).
Calculates and displays:
The total expenses in a given period (e.g., the last 6 months).
The average monthly expense.
The remaining savings after expenses for the last 6 months.
Calculates the percentage of savings left compared to the initial amount.'''

import math

savings = int(input("Please enter your initial savings amount: "))
num_months = int(input("how many month of expenses do you want to track? "))
expenses = []

for i in range(1, num_months + 1):
    expense = float(input(f"Enter your expenses for month {i}: "))
    expenses.append(expense)

print(f"Total expenses for {num_months} months: {math.fsum(expenses)}")
print(f"Average monthly expense: {math.fsum(expenses) / len(expenses)}")
print(f"Remaining savings: {savings - math.fsum(expenses)}")
print(f"Now {((float(savings) - math.fsum(expenses)) / savings) * 100} % of your savings are remaining.")


'''Getting all the files of the working directory with their last modified times.'''

import os
import datetime
alldirs = os.listdir()
dirs = {}

for file in alldirs:
    dirs.update({f"{datetime.datetime.fromtimestamp(os.path.getmtime(file))}" : f"{file}"})


# Randomized Team Assignment using random module

import random

trainees = ["Anuvansh", "Harsimran", "Parth", "Sameer", "Ankush", "Daljeet", "Abhishek", "Naman", "Shyam"]

def distribute_randomly(list, team_size):
    random.shuffle(list)
    result = []
    
    for i in range(0, len(list), team_size):
        result.append(list[i : i + team_size])
        
    return result

teams = distribute_randomly(trainees, 4)
for team in teams:
    print(team)



# Random weather forecast generator for next n days

import datetime
import random

def random_weather_forecast(days):
    
    weather = ["sunny", "rainy", "cloudy"]
    
    print(f"Weather forecast for the next {days} days-")
    
    for i in range(1, days +1):
        current_date = datetime.date.today()
        print(f"{current_date + datetime.timedelta(days = i)} : {random.choice(weather)}")


random_weather_forecast(10)

'''Some funtions of os moudle'''
import os

print(os.getcwd())
# os.mkdir("testosmod")
# os.rename("censor.txt", "censored.txt")
os.remove("testosmod")

#Generating n random numbers between a range
import random

for i in range(10):
    print(random.randint(1, 100))

#ceiling and floor of a number
import math
a = 1.2
print(math.ceil(a))
print(math.floor(a))

'''Exercise 5: Combining Modules (math, os, and random)
Task: Write a Python program that:
-Creates a folder called RandomFiles if it doesn’t exist.
-Generates 5 random numbers between 1 and 100.
-Creates a text file for each of the 5 random numbers, naming the files as number.txt (e.g., 34.txt, 57.txt).
-Writes the square root of each number to its respective file.
-Lists all the files created and displays the contents of each file.'''

import random, os, math

os.mkdir("RandomFiles")

for i in range(5):
    
    num = random.randint(1, 100)
    print(f"random number is {num}")
    
    with open(f"RandomFiles/{num}.txt", "w") as f:
        f.write(f"{math.sqrt(num)}")
    print(f"{num}.txt file is created successfully in 'RandomFiles' folder.")
    
print(os.listdir("RandomFiles"))


