# from arithmetic_operations import perform_operation
# try:
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))
#     operation = input('Enter operation (+,-,*,/): ')
#     result = perform_operation(num1,num2,operation)
#     print('Result:',result)
# except ValueError:
#     print('Invalid input. Please enter valid numbers.')
# except Exception as e:
#     print('An error occurred:',str(e))


from arithmetic_operations import perform_operation


def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input(
        "Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
