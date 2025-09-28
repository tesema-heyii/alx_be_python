# def perform_operation (num1:float,num2:float,operation:str) -> str | float:
#     allowed_operations = ['+','-','*','/']
#     if operation not in allowed_operations:
#         return 'Invalid operation. please use one of +,-,*,/'
#     if operation == '+':
#         return num1 + num2
#     elif operation == '-':
#         return num1 - num2
#     elif operation == '*':
#         return num1 * num2
#     elif operation == '/':
#         if num2 == 0:
#             return 'Division by zero is not allowed'
#         return num1 / num2


def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation on two numbers.

    This function takes two numbers and an operation name as input,
    then returns the result of the specified operation. It handles
    addition, subtraction, multiplication, and division, including
    a check for division by zero.

    Args:
        num1 (float): The first number for the operation.
        num2 (float): The second number for the operation.
        operation (str): The name of the operation to perform.
                         Accepts 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The numerical result of the operation, or a
                      string message if an error occurs (e.g., division
                      by zero or an invalid operation).
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Check for division by zero before performing the operation.
        if num2 == 0:
            return "Error: Cannot divide by zero."
        else:
            return num1 / num2
    else:
        # Return a message for any unspecified operations.
        return "Error: Invalid operation specified."
