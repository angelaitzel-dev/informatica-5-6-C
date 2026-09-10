def main():
    numbers= [1,2,3,4,5,6,7,8,9,10,11]
    resultm = max(numbers)
    print(resultm)
    results = sum(numbers)
    print(results)
    resultsmin = min(numbers)
    print(resultsmin)

    #red
    lista =["Rojo","Amarillo","verde"]
    print("lista:", lista)

    lista.pop(1)
    print("con pop(1):",lista)

    lista.remove("Rojo")
    print("con remove(´Rojo´):",lista)


if __name__ == "__main__":
    main()

