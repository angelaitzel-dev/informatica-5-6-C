def main():
    miau = True
    while miau:
        welcome()
        try:
            order = int(input("Select Your order: "))
            get_item(order)
            miau = False
        except ValueError:
            print("Try again looser")

def get_item(order):
    if order == 1:
        print("Here you go")
        print("🍟")
    elif order == 2:
        print("Here you go")
        print("🍔")
    elif order == 3:
        print("Here you go")
        print("🥤")
    elif order == 4:
        print("Here you go")
        print("🍦")
    elif order == 5:
        print("Here you go")
        print("🍪")
    else:
        print("Why are you like this?")

#def get_item(order):
    # kitchen = [menu items lol]
    # print(kitchen{order-1})

def welcome():
    menu = ["Fries","Cheeseburger","Soda","Ice Cream", "Cookie"]
    print("Welcome to the out and in restaurant!")
    print("")
    print("Here's the menu:")
    for gg in range(len(menu)):
        print(f"{gg+1}. {menu[gg]}")





if __name__ == "__main__":
    main()
