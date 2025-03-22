def divide(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return round(a / b, 2)

def exponentiate(a, b):
    return round(a ** b, 2)

def remainder(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return round(a % b, 2)

def summation(a, b):
    if a > b:
        print("Error: Second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\n===================================")
        print("MATHEMATICAL OPERATIONS MENU")
        print("===================================")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        print("===================================")
        
        choice = input("Enter your choice: ").strip().upper()
        print("===================================")
        
        if choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        
        if choice not in ['D', 'E', 'R', 'F']:
            print("Invalid choice. Please try again.")
            continue
        
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        
        if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
            print("Invalid input! Please enter numeric values.")
            continue
        
        num1, num2 = float(num1), float(num2)
        print("===================================")
        
        if choice == 'D':
            result = divide(num1, num2)
        elif choice == 'E':
            result = exponentiate(num1, num2)
        elif choice == 'R':
            result = remainder(num1, num2)
        elif choice == 'F':
            result = summation(int(num1), int(num2))
        
        if result is not None:
            print("===================================")
            print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()
