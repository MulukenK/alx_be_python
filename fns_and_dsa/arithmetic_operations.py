def perform_operation(num1, num2, operation):
   
        if operation == "":
            print("Please select an operation")
        elif operation == "add":
           return result = num1 + num2
        elif operation == "subtract":
            return result = num1 - num2
        elif operation == "multiply":
            return result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                return result = num1/num2
                