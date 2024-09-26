FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

temperature = int(input("Enter the temperature to convert:"))

conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()



if conversion == "f":
    if 32 <= temperature <= 212:
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")
        
elif conversion == "c":
    if 0 <= temperature <= 100:
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    
    else:
        print("Invalid temperature. Please enter a numeric value.")

else:
    print("Please enter a correct scale (Fahrenheit or Celsius).")



   