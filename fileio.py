#File Handling 

#Reading from a file
file = open("sample.txt")
data = file.read()
print(data)

file.seek(0)   #after read() the pointer reaches the end of file and after this any read opeartion will return empty strings, so we use seek(0) to shift the pointer to the start.

#Reading lines from a file
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()

print(f"Line1: {line1}")
print(f"Line2: {line2}")
print(f"Line3: {line3}")

file.seek(0)
#creating a list containing each line of the file
lines = file.readlines()
print(lines)

file.close()

#Writing to a file
file = open("sample2.txt", "w")

str = "Hi! This is just a sample string which is to be written in a file."

file.write(str)
file.write("\nThank You\nHave a Nice Day!")

str_list = ["\nThis is a line.\n", "this is also a line.\n", "Hey! i am another line.\n"]
file.writelines(str_list)

file.close()

# Modes of opening a file

# read mode(r)-default
file = open("sample.txt", "r" )
content = file.read()

print(content)
file.close()

# write mode(w)
file = open("sample2.txt", "w")
file.write("hello i am writing to this file.")

file.close()

# append mode(a)
file = open("sample2.txt", "a")
file.write("This line was written using append mode.")

print(file.tell()) #tell() returns the file pointer's current position
file.close()

# with statement- automatically closes the file after program ends.
with open("sample.txt") as f:
    print(f.read())

#Practice Questions-
'''1. WAP to write Twinkle twinkle little stars poem in a file named poem.txt
    Then write a program to find if 'twinkle' word existsin the poem.txt file or not.
'''

with open("poem.txt", "w") as f:
    poem = "Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky."

    f.write(poem)

with open("poem.txt") as f:
    content = f.read()
    if ("twinkle" in content.lower()):
        print("The word 'twinkle' is present in the file.")

    else:
        print("The word 'twinkle' is not present in the file.")


'''2.The game function in a program lets user play a game and returns the score as an integer.
    You need to read a file 'Hi-Score.txt' which is either blank or contains the previous Hi-Score.
    You need to WAP to update the HI-Score whenever the game() breaks the highscore.
'''
import random

def game():
    
    print("YOU ARE PLAYING THE GAME...")
    
    score = random.randint(1, 70)
    print(f"Your score is {score}.")
    
    return score

with open("hiscore.txt") as f:
    hiscore = f.read()

    if (hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0

score = game()

if score > hiscore or hiscore == 0:
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

'''3.WAP to print multiplication tables of 2 to 20 and store them in separate files.
    Compile these files into a folder.'''

def gentable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"
    
    with open(f"tables/table_of_{n}", "w") as f:
        f.write(table)

for i in range(2, 21): 
    gentable(i)


'''4.A file contains "Donkey" word multiple times, 
you have to replace this word with ##### by updating the same file.'''

with open("donkey.txt") as f:
    content = f.read()

    new_content = content.replace("Donkey", "######")

with open("donkey.txt", "w") as f:
    f.write(new_content)

'''5.Repeat the above program to censor a list of words'''

bad_words = ["badword1", "badword2", "badword3"]

def censortxt(file, unwanted_words):
    with open(file) as f:
        content = f.read()

        for word in bad_words:
            content = content.replace(word, "*" * len(word))

    with open(file, "w") as f:
        f.write(content)

    print("Censorship Complete! ALl unwanted words are removed from the text.")

censortxt("censor.txt", bad_words)


##Working with CSV Files using csv module
import csv

with open("test.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Age", "City"])
    csv_writer.writerow(["Anuvansh", "21", "Lalru"])
    csv_writer.writerow(["Shyam", "24", "Mohali"])
    csv_writer.writerow(["Alice", "23", "Mumbai"])

with open("test.csv") as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        print(row)

with open("test.csv") as file:
    csv_reader = csv.DictReader(file) #reads each row into a separate dictionary, headers are the keys

    for row in csv_reader:
        print(row["Name"], row["Age"], row["City"])

