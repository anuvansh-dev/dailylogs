"""
User will input (3 ages).Find the oldest one
"""


# def find_oldest():
#     try:
#         age1 = int(input('Enter age: '))
#         age2 = int(input('Enter age: '))
#         age3 = int(input('Enter age: '))
        
#         if age1 > age2 and age1 > age3:
#             return f"age1({age1}) is the oldest."
#         elif age2 > age1 and age2 > age3:
#             return f"age2({age2}) is the oldest."
#         else:
#             return f"age3({age3}) is the oldest."
    
#     except ValueError:
#         print("Please enter an integer value, age cannot be string.")
#         return find_oldest()

# print(find_oldest())

# Using list and foor loop
def find_oldest():
    age = []
    for i in range(3):
        age.append(int(input("Enter age: ")))
    age.sort(reverse=True)
    return age[0]

print(find_oldest())