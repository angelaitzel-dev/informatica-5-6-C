def main():
    # Augmented Assignment Operator
    money = 5
    money += 10
    print(money) #this will print 15

    #Substraction assignment operator
    minutes = 60
    minutes -= 25
    print(minutes)
    #this will print 35

    #Multiplication assignment Operator
    skill = 10
    skill *=2
    print(skill)

    text = "Hello"
    text *= 20
    print(text)

    #Division assignment operator
    pizzas = 8
    people = int(input("Number of People at the party: "))
    pizzas /= people
    print(pizzas)

    # Modulus Assignment Operator
    leftover = 8
    leftover %= people
    print(leftover)

if __name__ == "__main__":
    main()
