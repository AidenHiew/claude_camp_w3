#calculator 

print("Welcome to the simple calculator!")

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid operator. Please try again.")
                continue

            print(f"The result of {num1} {operator} {num2} is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

            