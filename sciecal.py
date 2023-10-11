import math

def main():
    print("Scientific Calculator")
    while True:
        print("Choose an option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation (x^y)")
        print("6. Square root (√x)")
        print("7. Trigonometric functions")
        print("8. Quit")
        choice = input("Enter your choice (1,2,3,4,5,6,7,8): ")

        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            exponentiation()
        elif choice == '6':
            square_root()
        elif choice == '7':
            trig_functions()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")

def add():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = convert_input(num1)
    num2 = convert_input(num2)
    result = num1 + num2
    print("Result: ", result)

def subtract():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = convert_input(num1)
    num2 = convert_input(num2)
    result = num1 - num2
    print("Result: ", result)

def multiply():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = convert_input(num1)
    num2 = convert_input(num2)
    result = num1 * num2
    print("Result: ", result)

def divide():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = convert_input(num1)
    num2 = convert_input(num2)
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result: ", result)

def exponentiation():
    base = input("Enter the base (x): ")
    exponent = input("Enter the exponent (y): ")
    base = convert_input(base)
    exponent = convert_input(exponent)
    result = base ** exponent
    print("Result: ", result)

def square_root():
    num = input("Enter the number (x) to find the square root of: ")
    num = convert_input(num)
    if num < 0:
        print("Error: Square root of a negative number is not real.")
    else:
        result = math.sqrt(num)
        print("Result: ", result)

def trig_functions():
    print("Trigonometric functions:")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    choice = input("Enter your choice (1/2/3): ")
    angle = input("Enter the angle in degrees: ")
    angle = convert_input(angle)

    if choice == '1':
        result = math.sin(math.radians(angle))
        print(f"Sine of {angle} degrees is: {result}")
    elif choice == '2':
        result = math.cos(math.radians(angle))
        print(f"Cosine of {angle} degrees is: {result}")
    elif choice == '3':
        result = math.tan(math.radians(angle))
        print(f"Tangent of {angle} degrees is: {result}")
    else:
        print("Invalid input. Please choose a valid option.")

def convert_input(input_str):
    if input_str.lower() == "pi":
        return math.pi
    return float(input_str)


main()