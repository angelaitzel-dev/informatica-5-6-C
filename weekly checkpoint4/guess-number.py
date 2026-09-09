import random

def main():
    name = input("Hello!, whats your name? ")
    print(f"Well, {name},  I am thinking of a number between 1 and 100.")
    guess = ""
    number = random.randint(1,100)

    while guess != number:
        guess = int(input("Take a guess: "))
        if guess > number:
            print("Your guess is too high")
        elif guess < number:
            print("Your guess is too low!")
        else:
            print(f"Congratulations {name}! You guessed my number!")


if __name__ == "__main__":
    main()

