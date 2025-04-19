#2.CALCULATOR

def calculator():
    print("Welcome to the Simple Calculator!")
    print("You can choose: + for addition, - for subtraction, * for multiplication, / for division")

    while True:
        # Input numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Choose operation
        operation = input("Choose an operation (+, -, *, /): ").strip()

        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        # Display result
        print(f"Result: {num1} {operation} {num2} = {result}")

        # Ask to calculate again
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator!")
            break

# Start the calculator
calculator()