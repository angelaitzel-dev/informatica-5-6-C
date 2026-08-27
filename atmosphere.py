def main():

    layer = input("Descent Atmosphere layer: ")
    if layer == "Exosphere":
        print("Your altitude level will be between 700 km and 10,000 km")

    elif layer == "Thermosphere":
        print("Your altitude level will be between 85 km and 700 km")

    elif layer == "Mesosphere":
        print("Your altitude level will be between 50 km and 85 km")

    elif layer == "Stratosphere":
        print("Your altitude will be between 12 km and 50 km")

    elif layer == "Troposphere":
        print("Your altitude will be between 12 km and 0 km")

    else:
        print("Invalid option")

    altitude = float(input("Enter your exact altitude: "))
    altitude *= 1000
    timea = 0
    timeb = 0
    timec = 0
    timed = 0
    timee = 0

    if layer == "Exosphere":
        timea = (altitude - 700000) / 2000
        timeb = (altitude - 785000) / 500
        timec = (altitude - 835000) / 200
        timed = 
        print(

    elif layer == "Thermosphere":
        print("Your altitude level will be between 85 km and 700 km")

    elif layer == "Mesosphere":
        print("Your altitude level will be between 50 km and 85 km")

    elif layer == "Stratosphere":
        print("Your altitude will be between 12 km and 50 km")

    elif layer == "Troposphere":
        print("Your altitude will be between 12 km and 0 km")

    else:
        print("Invalid option")





if __name__ == "__main__":
    main()
