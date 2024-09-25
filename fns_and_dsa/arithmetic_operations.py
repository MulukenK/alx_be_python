def perform_operation(num1, num2, operation):
    match operation:
        case "add":
           return result = num1 + num2
        case "subtract":
            return result = num1 - num2
        case "multiply":
            return result = num1 * num2
        case "divide":
            if num2 != 0:
                return result = num1/num2
            else:
                print("Cannot divide by zero")