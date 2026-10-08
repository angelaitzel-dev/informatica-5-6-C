def main():

    print("Binary to Decimal Converter")

    print("")

    print("We're here to convert your binary numbers to decimal numbers")

    print("")
    miau = True
    while miau:
        try:
            binary = int(input("Enter your binary number = "))
            miau = False
        except ValueError:
            print("Why are you like this?")
    print("Miau")
    binary_to_decimal(binary)

def binary_to_decimal(binary):
    print("")

if __name__ == "__main__":
    main()

