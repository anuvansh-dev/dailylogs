
def top_three_letters(word):
    """
    Finds and returns the top three most occurring letters in a given string.

    The function counts the frequency of each unique letter in the string 
    and sorts them in descending order of frequency. If multiple letters 
    have the same frequency, they are sorted alphabetically.

    Args:
        word (str): The input string from which letter occurrences are counted.

    Returns:
        list: A list of dictionaries, each containing:
            - 'letter' (str): The letter itself (in lowercase).
            - 'count' (int): The frequency of the letter.

    Notes:
        - The function converts the string to lowercase before processing.
    """
    # converts input string to lowercase
    word = word.lower()
    letter_count = []
    
    # a temp variable for handling the uniqueness of letters in the list
    temp = ""

    for letter in word:
        if letter not in temp:
            temp += letter
            letter_count.append({"letter": letter, "count": word.count(letter)})

    # used two keys in sort() for handling letters having same count, '-' stands for reverse order
    letter_count.sort(key=lambda x: (-x['count'], x['letter']))

    # extracting top 3 values
    result = letter_count[0:3]
    return result

# Testing the function for 'Mooglelabs'
top_letters = top_three_letters('MoogleLabs')
   
print("Top 3 letters:-")

for i in top_letters:
    print(f"{i['letter']} : {i['count']}")