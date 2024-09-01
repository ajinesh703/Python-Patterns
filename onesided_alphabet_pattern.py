n = 5  # Number of rows

# ASCII value of 'A' is 65
ascii_value = 65

for i in range(n):
    for j in range(i + 1):
        print(chr(ascii_value + j), end=" ")
    print()
