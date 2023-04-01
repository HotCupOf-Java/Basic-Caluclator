#Functions to use in the calc: Add, Subtract, Multiply, Divide, and exit.
#This will be printed to the console.
#User will input the values, and select options

def add(a,b):
    answer = a + b
    return print(f"{a} + {b} = {answer}")

def subtraction(a,b):
    answer = a - b
    return print(f"{a} - {b} = {answer}")

def multiplication(a,b):
    answer = a * b
    return print(f"{a} * {b} = {answer}")

def division(a,b):
    answer = a / b
    return print(f"{a} / {b} = {answer}")


while True:

    print("Please choose one of the following:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("E. Exit the program")

    choice = input("What method would you like to use?: ")

    if choice == "1":
        print("Addition: ")
        a = int(input("The first number: "))
        b = int(input("The second number: "))
        add(a,b)
    elif choice == "2":
        print("Subtraction: ")
        a = int(input("The first number: "))
        b = int(input("The second number: "))
        subtraction(a,b)
    elif choice == "3":
        print("Multiplication: ")
        a = int(input("The first number: "))
        b = int(input("The second number: "))
        multiplication(a,b)
    elif choice == "4":
        print("Subtraction: ")
        a = int(input("The first number: "))
        b = int(input("The second number: "))
        division(a,b)
    elif choice == "e" or "E":
        print("Goodbye!")
        quit()

