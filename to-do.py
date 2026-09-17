
def main():
    tasks= []
    answer= ""
    ask = ""
    while True:
        answer = input("Do you want to: complete a task, add a task, or exit? ").strip().lower()
        if answer == "add":
            tasks.append(input("Add a task to the list: "))
            print(tasks)
        elif answer == "complete":
            ask = input("Have you finshed all of them?").strip().lower()
            if ask == "yes":
                tasks.clear()
                print("You finished all of them!")
                break
            else:
                tasks.remove(input("What did you finish?"))
                print(tasks)
            if tasks == []:
                print("You finished!")
                break
        elif answer == "exit":
            break
        else:
            print("Why are you like this?")
            break
if __name__ == "__main__":
    main()
