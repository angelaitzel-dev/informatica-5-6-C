def main():
    height = int(input("Give me a height?"))
    asterisk = "*"
    for miau in range(height):
        print(asterisk * (miau+1))
if __name__ == "__main__":
    main()
