import random

def main():
    guess= input("Guess the coin flip: ")
    coin = random.randint(1,2)
    coin2 = "blank"
    if coin == 1:
        coin2 = "Heads"
        print(f"{coin2}")
        if guess == coin2:
            print("You won")
        else:
            print("You Lost")
    elif coin == 2:
        coin2 = "Tails"
        print(f"{coin2}")
        if guess == coin2:
            print("You Won")
        else:
            print("You Lost")

if __name__ == "__main__":
    main()

