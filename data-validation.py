def main():
    #number= input("Enter a number: ") "1"
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1-10: "))
            if 1<= number <= 10:
                print("Number stored successfully.")
                not_validated = False
            else:
                print("Enter a NUMBER between 1-10 😒")
        except ValueError:
            print("Enter a NUMBER 😒")
    while True:
        
if __name__ == "__main__":
    main()
