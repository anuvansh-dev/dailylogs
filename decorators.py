#decorators provide us with the ability to add extra features to an existing funtion without accessing or modifying it.
def div(a, b):
    return a/b

#now we want our values to be swapped if the numerator is larger than the denominator, for this we'll use decorators.

def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    
    return inner

div = smart_div(div)

print(div(2, 4))

