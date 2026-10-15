import random
def main():
    start_game("words.txt")
def start_game(file):
    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank)
    attempts = 10
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
        print("Current word:", " ".join(hint))
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")
        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great Guess!")
        elif guess in hint:
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")
        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", word)
            break
        if attempts == 0 and "_" in hint:
            print("No attempts left 💀 The word was:", word)
if __name__ == "__main__":
    main()




# import random
# def main():
#     with open("words.txt") as file:
#         start_game("words.txt")

# def start_game(a):
#     with open(a) as file:
#         words = file.read().splitlines()
#         word = random.choice(words)
#     print(word)



# if __name__ == "__main__":
#     main()
































# do an import random to have the random words
# create a txt file with all the words
# define the main function
# put a welcoming message to proceed
# if the user chooses to, proceed
# If the user chooses to, break the cycle
# Turn the txt file into a list
# Define another function to avoid a lot of text
# Use the with to open the txt file in the function
# Use the rand to choose the word randomly
# use a while loop to keep the user playing
# use a  number variable to see the lives the user still has
# turn the letters into a list with len
# use a for loop to display to the user how many letters are in the word with a "_"
# get the user to input a letter
# use if then and in statementsto see if any letter is in the list made by the word
# Use an elif statement if no letter matched in the file to add one body part to the hangman or take away one live of the user
# When the word is complete break the loop and then if it is complete print "You Won"
# If the user runs out of lves print the word normally then break the loop with a "you lost"
# if the user puts any other repeated letter make sure to let them know
# make a letter bank for letters already used
