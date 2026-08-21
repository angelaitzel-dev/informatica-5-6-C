def main():
    years= int(input("How many years do you want to see into the future?: "))
    transistors = 178000002000
    current_year = 2026


    if (current_year + years) >= 2030:
        print("The law is not valid.")
    else:
        years /= 2
        transistors *= (2**years)
        transistors = round(transistors)
        print(f"This is the prediction for the future: {transistors}")


if __name__ == "__main__":
    main()
