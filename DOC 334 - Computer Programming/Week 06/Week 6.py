# Create a 2x3 matrix
matrix = []

# Get user input for matrix elements
for i in range(2):
    row = []
    for j in range(3):
        value = int(input(f"Enter the value for element ({i}, {j}): "))
        row.append(value)
    matrix.append(row)

# Get user input for multiplication factor
multiplier = int(input("Enter the value to multiply the matrix elements by: "))

# Multiply matrix elements by the multiplier
for i in range(2):
    for j in range(3):
        matrix[i][j] *= multiplier

# Print the updated matrix
for row in matrix:
    print(row)                          
