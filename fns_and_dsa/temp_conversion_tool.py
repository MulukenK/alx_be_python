FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

conversion = input("Pick what measure you want to convert to (Fahrenheit/Celsius): ").lower()

temperature = int(input("Enter temperature: "))

if conversion == "fahrenheit":
    if 0 <= temperature <= 100:
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    else:
        print("Please enter a temperature between 0 and 100°C.")
        
elif conversion == "celsius":
    if 32 <= temperature <= 212:
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    else:
        print("Please enter a temperature between 32 and 212°F.")
else:
    print("Please enter a correct measurement (Fahrenheit or Celsius).")