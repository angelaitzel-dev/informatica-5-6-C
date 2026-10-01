def main():
    print("Welcome to the times table quiz")
    times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
    max_value = int(input("How many times you want your table to continue?"))


    if 1 <= times_table <= 10:

        print(f"Here is the {times_table} times table")

        for x in range(1, max_value +1):
            answer = x * times_table
            print(f"{x} times {times_table} is {answer}")
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
