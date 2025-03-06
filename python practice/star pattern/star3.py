"""
****
***
**
*
"""

n = 4
for row in range(n):
    for col in range(1, n + 1 - row):
        print("* ", end="")
    print("\n")
        