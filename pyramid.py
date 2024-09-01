n = 5  # Number of rows

# ASCII value of 'A' is 65
ascii_value = 65

for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    # Print alphabet pattern
    for j in range(i + 1):
        print(chr(ascii_value + j), end=" ")
    # Print reversed alphabet pattern
    for j in range(i - 1, -1, -1):
        print(chr(ascii_value + j), end=" ")
    print()
