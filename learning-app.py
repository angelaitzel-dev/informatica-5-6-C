import random

def main():

    number1 = 0
    number2 = 0
    result = number1 + number2
    prompt = ""
    correct = ("Your answer is correct!")
    incorrect = ("Your answer is wrong")
    streak = 0
    star = "⭐"

    print("Addition for dummies")
    print("")


    while prompt != result:

        number1 = random.randint(10,99)
        number2 = random.randint(10,99)
        result = (number1 + number2)
        print(f"What is {number1} + {number2}?")
        prompt = int(input("Your answer = "))
        if prompt == result:
            print(f"{correct}")
            streak = star
            print(f"Streak: {streak}")
        if prompt != result:
            print(f"{incorrect}")
            streak = 0
            print("Streak lost")

    while prompt != result:
        number1 = random.randint(10,99)
        number2 = random.randint(10,99)
        result = (number1 + number2)
        print(f"What is {number1} + {number2}?")
        prompt = int(input("Your answer = "))
        if prompt == result:
            print(f"{correct}")
            streak = star
            print(f"Streak: {streak}")
        if prompt != result:
            print(f"{incorrect}")
            streak = 0
            print("Streak lost")





if __name__ == "__main__":
    main()
