def main():
    years= int(input("How many years do you want to see into the future?: "))
    transistors = 178000002000
    years /= 2
    transistors *= (2**years)
    transistors = round(transistors)
    print(f"This is the prediction for the future: {transistors}")

if __name__ == "__main__":
    main()
