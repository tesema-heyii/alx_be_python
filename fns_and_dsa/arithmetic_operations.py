def perform_operation (num1:float,num2:float,operation:str) -> str | float:
    allowed_operations = ['+','-','*','/']
    if operation not in allowed_operations:
        return 'Invalid operation. please use one of +,-,*,/'
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return 'Division by zero is not allowed'
        return num1 / num2


