def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Modulus by zero is not allowed"
    return x % y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

while True:
    try:
        choice = int(input("Enter operation you want to perform : "))

        if choice == 0:
            break

        if choice < 1 or choice > 5:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5/0 to exit)")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            result = divide(num1, num2)
            print("Result:", result)
        elif choice == 5:
            result = modulus(num1, num2)
            print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

