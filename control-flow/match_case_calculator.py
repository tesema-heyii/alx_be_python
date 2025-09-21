# match_case_calculator.py

try:
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user for the operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using match case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")

except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
