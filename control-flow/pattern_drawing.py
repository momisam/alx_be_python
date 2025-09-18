# Draw a square pattern of '*' using a while loop (rows) and a nested for loop (columns)

size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row +=1
        