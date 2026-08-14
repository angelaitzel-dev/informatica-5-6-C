def main():
    # planet = input("Planet: ")

    # #Separation
    # print("Hello", planet)

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    # #Concatenation
    # print("Hello " + planet)

    # # Formatted String
    # print(f"Hello {planet}")

    name = input("What's your name? ").title().strip()
    color = input("Tell me a color:").lower().strip()
    adjective = input("Give me an adjective:").lower().strip()
    goal = input("Tell me a goal you want to achieve:").lower().strip()
    print()
    print("Hello", name)
    print()
    print("This is your story:")
    print()
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")
    print()
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.".upper())

if __name__ == "__main__":
    main()
