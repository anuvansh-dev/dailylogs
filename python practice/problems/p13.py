"""
WAP to remove first n from given string 'learning' and print the result
"""

# word = "learning"
# result = ""
# flag = 0

# for letter in word:
#     if letter == "n" and flag == 0:
#         flag = 1
#         continue
#     result += letter


"""
WAP to remove second n from given string 'learning' and print the result
"""    
# word = "learning"
# result = ""
# flag = 0

# for letter in word:
#     if letter == "n" and flag == 0:
#         flag = 1
#     elif letter == "n" and flag == 1:
#         continue
#     result += letter

# print(result)

"""
using replace()
"""

# word = "learning"
# result = word.replace("n", "", -1)
# print(result)
# word.find()

"""
Using a list instead of string to save time as string is an immutable dtype thats why in every iteration a new result string is being created
"""
word = "learning"
result = []
counter_n = 0

for letter in word:
    if letter == "n":
        counter_n += 1
        if counter_n == 2:
            continue
    result.append(letter)
    
print("".join(result))
            