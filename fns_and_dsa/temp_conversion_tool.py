# temp_conversion_tool.py

# 1. Define Global Conversion Factors
# These variables are in the global scope, accessible to all functions in this file.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    
    Args:
        fahrenheit (float): The temperature in degrees Fahrenheit.
        
    Returns:
        float: The equivalent temperature in degrees Celsius.
    """
    # Accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR for reading.
    # No 'global' keyword is needed because we are not modifying the variable.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    
    Args:
        celsius (float): The temperature in degrees Celsius.
        
    Returns:
        float: The equivalent temperature in degrees Fahrenheit.
    """
    # Accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR for reading.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


# Main part of the script for user interaction
if __name__ == "__main__":
    try:
        # 3. Prompt the user to enter a temperature.
        temp_input = float(input("Enter the temperature to convert: "))

        # Prompt the user to specify the unit.
        unit = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Call the appropriate conversion function based on the user's input.
        if unit == 'F':
            converted_temperature = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {converted_temperature}°C")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {converted_temperature}°F")
        else:
            # Handle invalid unit input.
            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        # Handle cases where the temperature input is not a number.
        print("Invalid temperature. Please enter a numeric value.")
