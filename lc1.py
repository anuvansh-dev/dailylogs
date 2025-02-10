# Problem- Merge two strings alternatively
#eg. str1 = abc and str2 = pqr then output should be "apbqcr" if strings are unequal in length then append the extra characaters in the end of the result.

def mergestrs(word1, word2):
    
    mergedstr = ""
    length = min(len(word1), len(word2))
    
    for i in range(length):
            mergedstr += word1[i] + word2[i]

    mergedstr += word1[length:]
    mergedstr += word2[length:]


    return mergedstr
    
  
print(mergestrs("ABCDEFGH", "PQRST"))

