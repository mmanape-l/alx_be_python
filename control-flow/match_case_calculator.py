def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Prompt for user input
    num1 = get_number("Enter the first number:")
    num2 = get_number("Enter the second number:")
    operation = input("Choose the operation (+, -, *, /):")

    # Perform the calculation using match case
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        case _:
            print("Invalid operation. Please choose one of +, -, *, /.")
            return

    # Output the result
    print(f"The result is {result}")

if __name__ == "__main__":
    main()