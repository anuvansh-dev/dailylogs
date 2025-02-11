from functools import reduce

def is_even(n):
    return n % 2 == 0

def add_all(a, b):
    return a + b

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x : x % 2 == 0, nums))
print(even_nums)

#doubling all the even numbers now using map()- it maps an exprression to all the elements in an iterable
doubles = list(map(lambda x : x + 2, even_nums))    #map(function, iterable)
print(doubles)


sum  = reduce(lambda a, b : a + b, doubles) #reduce(function, sequence)- applies a function on all elements cumulatively i.e on first two then their result to the next element.
print(sum)