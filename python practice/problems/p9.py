"""
WAP that take a user input of three angles and will
find out whether it can form a triangle or not.
"""

def is_triangle(angle1, angle2, angle3):
    if (angle1 + angle2 + angle3) == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
        return True 
    else:
        return False

print(is_triangle(90, 45, 45))
print(is_triangle(90, 90, 10))
    