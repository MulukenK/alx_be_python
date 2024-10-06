def safe_divide(numerator, denominator):
    float(numerator)
    float(denominator)
    try:
        denominator == 0
        numerator or denominator != type(float)

    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    
    else:
        print(f"The result of the division is {numerator/denominator}")