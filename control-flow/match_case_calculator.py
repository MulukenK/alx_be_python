num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        output = num1 +num2
        print(f"The result is: {output}.")
    
    case "-":
        output = num1 - num2
        print(f"The result is; {output}.")

    case "*":
        output = num1 - num2
        print(f"The result is: {output}.")

    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            
        else:
            output = num1/num2
            print(f"The result is: {output}.")