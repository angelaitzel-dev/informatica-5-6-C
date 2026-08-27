def main():
    numberA = float(input("Type in your first number: "))
    numberB = float(input("Type in your second number: "))
    operation = input("Type if you want to add, subtract, multiply, or divide? ")
    result = 0
    if operation == "add":
        result = numberA + numberB
        print(f"{result}")

    elif operation == "subtract":
        result = numberA - numberB
        print(f"{result}")

    elif operation == "multiply":
        result = numberA * numberB
        print(f"{result}")

    elif operation == "divide":
        result = numberA / numberB
        print(f"{result}")

    else:
        print("Why are you like this?")
if __name__ == "__main__":
    main()
