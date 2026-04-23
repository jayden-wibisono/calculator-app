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
        return "You can't divide by zero"
    
def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

def menu_options():
    print("===Simple Calculator CLI===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Modulo")
    print("7. Exit")

while True:
    menu_options()

    option = input("What do you want to calculate? (1-7): ")

    if option == "7":
        print("===The Program Ends===")
        break
    
    if option not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid Option")
        continue
    
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
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
    
    print(f"Result = {result}")
    
    continue_or_not = input("Do you want to continue? (y/n): ")
    if continue_or_not == 'n':
        print("===The Program Ends===")
        break
    else:
        continue