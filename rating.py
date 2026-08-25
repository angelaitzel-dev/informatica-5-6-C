def main():
    print("Tacos de tres pesos")
    rating = float(input("How would you rate your dining experience in a 0-5 scale?:"))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")

    print("Thank you for dining with us")

if __name__ == "__main__":
    main()

