"""
Write a program that will convert celsius value to fahrenheit
"""

def celsius_to_fahrenheit(C):
    F = (C * (9 / 5)) + 32
    # return f"{(C*(9/5))+32}"
    return F

print(celsius_to_fahrenheit(30))