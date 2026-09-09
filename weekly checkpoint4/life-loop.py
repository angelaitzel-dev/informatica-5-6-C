import random
import time

def main():
    uplift = ["Keep Going!", "Don't give up!", "You're doing great!", "Small progress is still progress!", "You got this!"]

    uplift1 = ["Almost there!", "The final stretch!"]

    dontstop = ["Even Einstein took breaks!", "Take a moment to breathe!", "Don't stop now!"]

    assignments = int(input("How many assignments do you have?"))

    work = ""

    message = ""
    uplift2 = ""
    dont = ""
    while assignments != 0:

        work = int(input("How many assignments have you completed?"))
        message = random.choice(uplift)
        uplift2 = random.choice(uplift1)
        dont = random.choice(dontstop)
        assignments -= work

        if assignments >= 3:
            print(f"{message}")

        elif assignments < 3:
            print(f"{uplift2}")

        if assignments == 0:
            print("You finished!")
            break

        if work == 0:
            print(f"{dont}")

        time.sleep(1)



if __name__ == "__main__":
    main()
