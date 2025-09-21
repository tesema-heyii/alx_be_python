# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print()  # Move to the next line after each row
    row += 1
