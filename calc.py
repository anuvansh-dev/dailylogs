# calc.py
# This is a module with basic arithematic functionalities like add, sub, mul, div, power

def add(*args):
    # sum = reduce(lambda a, b : a + b, *args) # we can also do this but for this we have to import reduce() from functools module 
    result = 0
    for num in args:
        result += num
    return result

def sub(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def mul(*args):
    result = 1
    for num in args:
        result *= num
    return result

def div(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

def power(a, b):
    return a ** b



