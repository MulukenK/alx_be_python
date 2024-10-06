def safe_divide(numerator, denominator):
    
    try:
        float(numerator)
        float(denominator)
        
        denominator != 0
        numerator or denominator == type(float)

    
    except ZeroDivisionError:
        return print("Error: Cannot divide by zero.")
    except ValueError:
        return print("Error: Please enter numeric values only.")
    
    else:
       return print(f"The result of the division is {numerator/denominator}")