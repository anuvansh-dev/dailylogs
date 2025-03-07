data = []
rows = int(input("Enter no of rows: "))
cols = int(input("Enter number of columns: "))

# Taking data inputs
for i in range(rows):
    row = list(map(int, input().split()))
    # Ensuring correct column count
    if len(row) != cols:
        print(f"You can add only {cols} values per row!")
    data.append(row)

# Sorting the data based on the input attribute number
sort_col = int(input("Enter an attribute number to sort: "))
sorted_data = sorted(data, key=lambda x: x[sort_col])

# Printing sorted data
for row in sorted_data:
    print(row)

