import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You can't divide by zero!"
    
def power(a, b):
    return a ** b

def modulo(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "You can't divide by zero!"
    
def square_root(n):
    try:
        return math.sqrt(n)
    except ValueError:
        return "Cannot take square root of negative number!"

def factorial(n):
    if not n.lstrip("-").isdigit():
        return "Factorial only works for integers!"
    n = int(n)
    if n < 0:
        return "Cannot take factorial of a negative number!"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
def menu_options():
    print("===Simple Calculator CLI===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Modulo")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Exit")

while True:
    menu_options()

    option = input("What do you want to calculate? (1-9): ")
    
    try:
        if option in ['1', '2', '3', '4', '5', '6']:
            a = float(input("Enter the first number: ").replace(",", "."))
            b = float(input("Enter the second number: ").replace(",", "."))
        elif option in '7':
            n = float(input("Enter the number: ").replace(",", "."))
        elif option in '8':
            n = input("Enter the number: ")
        elif option == '9':
            print("===The Program Ends===")
            break
        else:
            print("Invalid Option")
            continue
    except ValueError:
        print("The input must be a number!")
        continue

    if option == '1':
        result = addition(a,b)
    elif option == '2':
        result = subtraction(a,b)
    elif option == '3':
        result = multiply(a,b)
    elif option == '4':
        result = division(a,b)
    elif option == '5':
        result = power(a,b)
    elif option == '6':
        result = modulo(a,b)
    elif option == '7':
        result = square_root(n)
    elif option == '8':
        result = factorial(n)
    
    print(f"Result = {result}")
    
    continue_or_not = input("Do you want to continue? (y/n): ").lower()
    if continue_or_not == 'n':
        print("===The Program Ends===")
        break
    else:
        continue