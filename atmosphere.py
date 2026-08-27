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
        print("Invalid option. Enter 0 ahead")

    altitude = float(input("Enter your exact altitude: "))
    altitude *= 1000
    timea = 0
    timeb = 0
    timec = 0
    timed = 0
    timee = 0
    timefinal = 0

    if layer == "Exosphere":
        timea = (altitude - 700) / 2000
        timeb = 615000 / 500
        timec = 35000 / 200
        timed = 38000 / 75
        timee = 12000 / 20
        timefinal = timea + timeb + timec + timed + timee
        timefinal = round(timefinal, 1)

        print(f"{timefinal}")

    elif layer == "Thermosphere":
        timeb = (altitude - 85000) / 500
        timec = 35000 / 200
        timed = 38000 / 75
        timee = 12000 / 20
        timefinal = timeb + timec + timed + timee
        timefinal = round(timefinal, 1)

        print(f"{timefinal}")

    elif layer == "Mesosphere":
        timec = (altitude - 50000) / 200
        timed = 38000 / 75
        timee = 12000 / 20
        timefinal = timec + timed + timee
        timefinal = round(timefinal, 1)

        print(f"{timefinal}")

    elif layer == "Stratosphere":
        timed = (altitude - 12000) / 75
        timee = 12000 / 20
        timefinal =timed + timee
        timefinal = round(timefinal, 1)

        print(f"{timefinal}")

    elif layer == "Stratosphere":
        timee = altitude / 20
        timefinal = round(timefinal, 1)

        print(f"{timefinal}")

    else:
        print("Not a valid option")


if __name__ == "__main__":
    main()
