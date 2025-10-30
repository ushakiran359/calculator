def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def main():
    print("===== SIMPLE CALCULATOR =====")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operation choice!")
if __name__ == "__main__":
    main()

