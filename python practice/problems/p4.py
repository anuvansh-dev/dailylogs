"""
WAP to sum all digits of a given number
"""
# Using list comprehension
# def add_digits(num):
#     num = str(num)
#     sum_of_digits = sum(int(digit) for digit in num)
#     return sum_of_digits


# Using loop and mod
def add_digits(num):
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num //= 10
        
    return sum_of_digits

print(add_digits(123))