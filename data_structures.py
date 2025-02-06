#Lists
list1 = [2, 5, 1, 28, 49, 74]
list1.append(75)
print(list1)
list1.remove(75)
print(list1)
print(list1[1:5]) #list slicing

#Sorting list
list1.sort()
print(list1)
list1.sort(reverse = True) # in descending order
print(list1)

#Write a program that merges two lists and removes duplicates using a set.
l1 = [1, 2, 3, 3, 4]
l2 = [5, 5, 6, 7, 7]

merged_list = set(l1 + l2)
print(merged_list)

#Write a program to create a new list with squares of each element from a given list of numbers.
def sqr(n):
    return n * n

l3 = [1, 2, 3, 4, 5]
sq_l3 = list(map(sqr, l3))
print(sq_l3)

# Creating a new list with squares of each element from an existing list using list comprehension
l4 = [1, 2, 3, 4, 5]
sq_l4 = [n * n for n in l4]
print(sq_l4)


# Dictionaries

dict1 = {"Anuvansh" : "SDE",
         "Rahul" : "QA",
         "Vimal": "IOS"
}

print(dict1.get("Anuvansh"))
print(dict1.get("Anu")) #error
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1["Rahul"])
dict1.pop("Vimal")
print(dict1.items())


dict1.update({"Rahul" : "Sr QA"})
print(dict1.items())
dict1.update({"Anu" : "Sr SDE", "Ankush" : "SDE"})
print(dict1.items())
print(dict1.get("Anu"))

# Create a program that counts the frequency of each character in a string
# and stores the result in a dictionary (key: character, value: frequency).
def char_freq(str):
    
    str = str.lower()
    frequency = {} 

    for i in str:
        freq = str.count(i)
        frequency.update({f"{i}" : f"{freq}"})

    return (frequency.items())

result = char_freq("Anuvansh")
print(result)

#Tuples

t = (1, 2, 3, "Four", 5.9, True, None)
print(t)
t.add("Five")
print(t)

t1 = (1, 1, 2, 3, 4)
n1, n2, n3, n4 = t1
print(n1, n2, n3, n4)
print(t1.count(1)) # prints how many times 1 occurs in tuple t1
print(t1.index(1))  # prints the index of first occurrence of 1 in t1

# Program to find min and max from a list of numbers and return them as values of a tuple.
def find_min_max(numbers):
    tup = (min(numbers), max(numbers))
    return tup
    
print(find_min_max([2, 6, 2, 1, 3]))


#Sets

s1 = {1, 2, 3, 3 ,4, 5}
s2 = {5, 6, 88, 9, 20}

print(s1.union(s2))
print(s1.intersection(s2))

# Creating a set of even numbers upto 20 using set comprehension
even_nums = {n for n in range(1, 21) if n % 2 == 0}
print(even_nums)