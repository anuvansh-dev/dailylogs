"""
WAP to reverse a given number,
And also returns true or false based on whether the reversed form is equal to the number itself
"""

def reverse(num):
    num = str(num)
    reversed = ""
    
    for digit in num[::-1]:
        reversed += digit
    
    return reversed, reversed == num 

print(reverse(121))