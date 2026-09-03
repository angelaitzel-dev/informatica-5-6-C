import random

def main():
    name = input("Hello!, whats your name? ").strip().title()
    difficulty = input((f"Well, {name},  I have a guessing game, do you wanna play easy, medium, or hard? ")).strip().title()
    guess = ""
    number = ""
        if difficulty == "Hard":
            number = random.randint(1,100)
            print("I am thinking of a number between 1 and 100")
            while guess != number:
                guess = int(input("Take a guess: "))
                if guess > number:
                    print("Your guess is too high")
                elif guess < number:
                    print("Your guess is too low!")
                else:
                    print(f"Congratulations {name}! You guessed my number!")
                    break
        elif difficulty == "Medium":
            number = random.randint(1,50)
            print("I am thinking of a number between 1 and 50")
            while guess != number:
                guess = int(input("Take a guess: "))
                if guess > number:
                    print("Your guess is too high")
                elif guess < number:
                    print("Your guess is too low!")
                else:
                    print(f"Congratulations {name}! You guessed my number!")
        elif difficulty == "Easy":
            number = random.randint(1,20)
            print("I am thinking of a number between 1 and 20")
            while guess != number:
                guess = int(input("Take a guess: "))
                if guess > number:
                    print("Your guess is too high")
                elif guess < number:
                    print("Your guess is too low!")
                else:
                    print(f"Congratulations {name}! You guessed my number!")
        else:
            print("Why are you like this?")


if __name__ == "__main__":
    main()


