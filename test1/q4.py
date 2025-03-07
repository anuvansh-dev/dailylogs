# Getting total number of stamps user want to enter as input
N = int(input("Enter total number of country stamps: "))

# Storing the country names in a set to get only distinct/unique values
stamps = set()

# Taking input(countries) from the user
for _ in range(N):
    stamp = input().strip()
    stamps.add(stamp)

# Printing number of distinct country stamps
print(len(stamps))