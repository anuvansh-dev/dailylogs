"""
WAP to check if a number is armstrong number
"""

def is_armstrong(num):
    temp = 0
    
    for digit in str(num):
        temp += (int(digit) ** len(str(num)))
    
    return True if temp == num else False

print(is_armstrong(123))