def main():
    colombian = int(input("How Many Colombian Pesos do you have left?"))
    peruvian = int(input("How Many Peruvian Soles do you have left?"))
    brazilian = int(input("How Many Brazilian Reais do you have left?"))
    ctomx = colombian / 183.3
    ptomx = peruvian * 5.07
    btomx = brazilian * 3.28
    ctous = colombian / 3131.81
    ptous = peruvian / 3.37
    btous = brazilian / 5.21
    mxn = round(ctomx + ptomx + btomx, 2)
    usd = round(ctous + ptous + btous, 2)
    print(f"MXN: ${mxn}")
    print(f"USD: ${usd}")
if __name__ == "__main__":
    main()
