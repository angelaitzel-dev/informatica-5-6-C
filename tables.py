def main():

    number = ""
    variable = 0
    while True:
        number = input("Do you want to continue or exit? ").strip().lower()
        if number == "continue":
            variable = int(input("What table from 1-10 do you want? "))
            if variable <= 10:
                print(f"The table of {variable}")
                for p in range(10):
                    print(f"{p+1} times {variable} is {(p+1)*variable}")
            if variable > 10:
                print("Why are you like this?")
                break
            if variable < 0:
                print("Why are you like this?")
                break
        elif number == "exit":
            print("GoodBye!")
            break
        else:
            print("Why are you like this?")
            break
if __name__ == "__main__":
    main()
