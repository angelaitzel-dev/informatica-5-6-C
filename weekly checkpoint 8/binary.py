def main():
    print("Binary to Decimal Converter")
    print("")
    print("We're here to convert your binary numbers to decimal numbers.")
    print("")
    miau = True
    while miau:
        try:
            binary = input("Enter your binary number = ")
            miau = False
        except ValueError:
            print("Why are you like this?")
    binary_to_decimal(binary)

def binary_to_decimal(binary):
    print("")
    reverse = range(len(binary))
    results = 0
    miau = 0
    for i in reverse:
        results = results + (int(i) * (2 ** miau))
        miau += 1
    print(f"Your {binary} is gonna be {results}")
if __name__ == "__main__":
    main()

