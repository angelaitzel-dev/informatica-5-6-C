def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    def highest(a,b):
        if a > b:
            highest_num = a
            print(f"The highest number is {highest_num}")
        elif b > a:
            highest_num = b
            print(f"The highest number is {highest_num}")
        else:
            print("Theyre the same number")
    # highest(8,2)
    highest(num1,num2)
    print("To check for the lowest number")
    num3 = int(input("Enter the first number: "))
    num4 = int(input("Enter the second number: "))
    num5 = int(input("Enter the third number: "))
    def lower(a,b,c):
        if a < b and a < c:
            lowest = a
            print(f"The lowest number is {lowest}")
        elif b < a and b < c:
            lowest = b
            print(f"The lowest number is {lowest}")
        elif c < a and c < b:
            lowest = c
            print(f"The lowest number is {lowest}")
        else:
            print("Theyre the same number")
    lower(num3,num4,num5)


if __name__ == "__main__":
    main()
