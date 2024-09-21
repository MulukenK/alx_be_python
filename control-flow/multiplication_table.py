number = int(input("Enter a number to see its multiplication table: "))

for number2 in range(1,10):
    result = number * number2
    print(f"{number} * {number2} = {result}", end = "\n")
