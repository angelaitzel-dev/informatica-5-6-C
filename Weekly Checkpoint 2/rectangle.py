def main():
    Width = int(input("What is the Width of the rectangle?"))
    print("O" * Width)
    print("O" * Width)
    print("O" * Width)
    print("O" * Width)
    print("O" * Width)
    Area = Width * 5
    print(f"This is the area of the rectangle: {Area}")
    Diagonal = (Width ** 2 + 5 ** 2)**0.5
    print(f"This is the rectangle's diagonal: {Diagonal}")
    perimeter = (Width + 5)*2
    print(f"This is the perimeter: {perimeter}")

if __name__ == "__main__":
    main()
