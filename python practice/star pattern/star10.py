"""
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
"""
n = 5

for i in range(n, 0, -1):
    print(" " * (n-i), end="")
    print("* " * i)
for j in range(1, n+1):
    print(" " * (n-j), end="")
    print("* " * j)