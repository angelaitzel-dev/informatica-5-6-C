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

    #Blue
    number = [1, 4, 5, 7, 9, 3]
    number.sort()
    print(number)

    #Yellow
    fruits = ["apple", "orange", "grapes"]
    fruits.append("banana")
    print(fruits)

    fruits1 = ["Apple", "Orange", "grapes"]
    fruits1.insert(2,"banana")
    print(fruits1)

    #green

    objects = ["Pencil", "Computer", "chair", "paper", "yoyo", "nickel"]
    objects[len(objects)-1] = "Rock"
    print(objects)
    print(len(objects))

if __name__ == "__main__":
    main()

