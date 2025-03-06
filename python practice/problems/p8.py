"""
WAP to calculate euclidean distance between two points
"""

from math import sqrt

def euclidean_distance(a, b):
    if type(a) == tuple and type(b) == tuple:
        result = sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))
        return result
    else:
        raise ValueError("Please give tuple values (x, y)")
    
print(euclidean_distance((4, 1), (3, 0)))