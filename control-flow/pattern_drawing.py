size = int(input("Enter the size of the pattern: "))

counter = 0

while counter <= size:
    for i in range(size):
        print("*", end="")
    counter += 1


    