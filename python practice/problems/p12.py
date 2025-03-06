"""
WAP to print first n terms of the Fibonacci series 
"""

# def fib(n):
#     result = [0, 1]
#     for i in range(2, n):
#         result.append(result[i - 2] + result[i - 1])
#     return result

def fib(n):
    try:
        a, b = 0, 1
        for _ in range(n):
            print(a, end=", ")
            a, b = b, a + b
        if n < 0:
            raise ValueError
    except TypeError or ValueError:
        print("Please Enter a +ve integer value")


fib("anu")