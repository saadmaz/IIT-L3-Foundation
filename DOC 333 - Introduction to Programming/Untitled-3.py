def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def power(a, b):
    return a ** b

def calculator():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting the calculator...")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result: ", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result: ", result)
        elif choice == '5':
            result = power(num1, num2)
            print("Result: ", result)
        else:
            print("Invalid input. Please try again.")


calculator()
