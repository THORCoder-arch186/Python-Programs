print("Hello! Welcome to my Calculator")

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, ^): ")
    
    if operation == "+":
        print("The result is:", num1 + num2)
    elif operation == "-":
        print("The result is:", num1 - num2)
    elif operation == "*":
        print("The result is:", num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("The result is:", num1 / num2)
            print("The remainder is:", num1 % num2)
    elif operation == "^":
        print("The result is:", num1 ** num2)
    else:
        print("Invalid operation")
    
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Goodbye! Thanks for using the calculator.")
        break