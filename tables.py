def main():

    number = 0

    while True:
        number = input("Do you want to continue or exit?").strip().lower()
        if number == "continue":
            for p in range(10):
                print(f"{p+1} times {number} is {(p+1)*number}")
            if number > 10:
                print("Why are you like this?")
                break
        elif number < 0:
            print("Why are you like this?")
            break
        elif number == "exit":
            print("GoodBye!")
            break
        else:
            print("Why are you like this?")
if __name__ == "__main__":
    main()
