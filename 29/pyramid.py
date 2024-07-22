n=int(input("enter the number of rows "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("enter the number of rows "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("#",end="")
    print()

n=int(input("enter the number of rows "))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for j in range(n-i-1):
        print(" ",end="")
    print()
n=int(input("enter the number of rows "))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i-1):
        print("+",end="")
    print()


def pyramid_pattern(rows):
    # Outer loop to handle number of rows
    for i in range(0, rows):
        # Inner loop to handle number of columns
        for j in range(0, rows - i - 1):
            print(end=" ")  # Print spaces for left pyramid
        # Inner loop to handle number of columns
        for j in range(0, i + 1):
            print("* ", end="")  # Print stars for right pyramid
        print("")  # Move to the next line
rows = 5
# Example usage:

pyramid_pattern(rows)
