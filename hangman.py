import random
def main():
    # with open("words.txt") as file:
    #     words = file.read().splitlines()
    #     word = random.choice(words)
    start_game("words.txt")

def start_game(a):
    with open(a) as file:
        words = file.read().splitlines()
        word = random.choice(words)
        print(word)



if __name__ == "__main__":
    main()


































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
#
