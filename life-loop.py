import random
import time

def main():
    start = 600
    uplift = ["Keep Going!", "Don't give up!", "You're doing great!"]
    uplift1 = "Almost there!"
    assignments = int(input("How many assignments do you have?"))
    work = ""
    message = random.choice(uplift)

    while assignments != 0:
        work = int(input("How many assignments have you completed?"))
        assignments -= work
        if assignments > 3:
            print(f"{message}")

        if assignments <= 3:

            print(f"{uplift1}")

        if assignments == 0:
            print("You finished!")
            break

        if work == 0:
            print("Don't stop working")



if __name__ == "__main__":
    main()
