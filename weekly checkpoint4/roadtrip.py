def main():
    answer = "" #initialize
    followup = ""

    while answer != "Yes!": #condition
        answer = input("Are we There Yet? ").strip().title() #Update
        if answer == "Yes":
            followup = input("Really? ").strip().title()
        if followup == "Yes!":
            break


    print("We just arrived")
if __name__ == "__main__":
    main()
