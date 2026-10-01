def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1-10: "))
            if number >= 1 and number <= 10:
                print("Number stored successfully.")
                not_validated = False
            else:
                print("Enter a NUMBER between 1-10 😒")
        except ValueError:
            print("Enter a NUMBER 😒")
    while True:
        try:
            name = input("Enter your Name: ")
            f_letter = name[0]
            print("Name stored succesfully.")
            break
        except IndexError:
            print("I SAID, enter your name")

if __name__ == "__main__":
    main()
