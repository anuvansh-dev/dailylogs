# Function to check if a number is prime or not
def chkprime(num):
    
    if num == 0 or num == 1:
        print("Its a special case! Neither prime nor composite!")

    factors = []
    for i in range (1, num + 1):
        if num % i == 0:
            factors.append(i)
            
    if len(factors) > 2:
        print("Its a composite number")
    else: 
        print("Its a prime number")
    
    print(f"factors are {factors}")

chkprime(10) 


##Arguments
#1. Positional arguments: passed in the order they appear in the function def.
def add(a, b):
    return a + b

result = add(2, 3) # 2 -> a and 3 -> b
print(result)

#2. Keyword Arguments: passed by directly specifying the parameter names. Order doesnt matter here
result = add(b=3, a=2)
print(result)

#3. Variable length arguments: used when we dont know in advance how many parameters will a function take.
# '*args' for positional and '**kwargs' for keyword arguments-
# '**kwargs' creates a dictionary of key(keyword)-value pairs).
# '*args' collects all positional arguments in a tuple.
def var_add(*args):
    return sum(args)

result = var_add(2, 3, 10, 27)
print(result)

# '**kwargs'
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value} ")

greet(name = "Anuvansh", age = 21)

#4. Default Arguments: Used to set a default value for a parameter which is used when no value is argument is passed to the func call.
def sayhi(name = "User"):
    print(f"Hi {name}! How are you ?")

sayhi()
sayhi("Shyam")


# Function which accepts a list of numbers and returns the minimum and max value as a tuple
def find_min_max(numbers):
    """Returns the minimum and maximum value from a list of numbers as a tuple.

    Parameters: 
    numbers(list) : List of numbers (int or float).

    Returns: 
    tuple: containing minimum and maximum value in the list.
    """
    tup = (min(numbers), max(numbers))
    return tup
    
print(find_min_max([2, 6, 2, 1, 3]))

# Function that takes a list of strings and returns a new list with the length of each string 
def str_list_len(str_list):
    """Returns a new list with the lengths of each string from a list of strings.

    Parameters: 
    str_list(list) : List of strings.

    Returns: 
    list: a list containing length of each string from the list of strings.
    """
    len_list =[]
    for item in str_list:
        len_list.append(len(item))

    return len_list

print(str_list_len(["Anuvansh", "Parth", "five", "Eight"]))

#Using lambda fucntion to create a multiply func
multiply = lambda a, b: a * b
print(multiply(2, 5))

# using lambda func in sorted() func to sort a list of tuples based on the second element of each tuple
l1 = [(2, 5), (0, 3), (5, 1)]

s_l1 = sorted(l1, key = lambda x: x[1]) 
print(s_l1)

# Scope of variables
# 1. Local- defined inside the function and cannot be accessed outside.
def greet():
    message = "Welcome"
    print(message)

greet() 
# print(message) # this will throw output as the message is local to the greet function

# 2. Global- Defined before the function definition and can be accessed from anywhere in the program.

message = "Hi,User!"
def greet():
    print(message)

greet() 




