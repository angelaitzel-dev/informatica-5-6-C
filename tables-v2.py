def main():
    print("Welcome to the times table Quiz.")
    not_validated = True
    score = 0
    while not_validated:
        try:
            times_table = int(input("Enter the number table that you would like to be tested on (1-10): "))
            if 1 <= times_table <= 10:
                while not_validated:
                    try:
                        max_value = int(input("Enter the maximum value for your times table:"))
                        print(f"Here is your quiz on the {times_table} times table.")
                        while not_validated:
                            try:
                                for x in range(1, max_value+1):
                                    answer = x * times_table
                                    useranswer = int(input(f"{x} times {times_table} is? "))
                                    not_validated = False
                                    if useranswer == answer:
                                        print("correct!")
                                        score += 1
                                    else:
                                        print("incorrect")
                            except ValueError:
                                print("You didn't enter a number")
                    except ValueError:
                        print("Enter a number")
            else:
                print("Invalid command.")
        except ValueError:
            print("You didn't enter a number to be quizzed on")
    print(f"Your Score was {score}/{max_value}")
if __name__ == "__main__":
    main()
