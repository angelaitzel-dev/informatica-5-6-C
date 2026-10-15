def main():
    # Read a File
    with open("sample.txt") as file:
        content = file.read()

        print(content)
    #Turn file into a list
    with open("sample.txt") as hoco_week:
        hoco_list = hoco_week.read().splitlines()
        print(hoco_list)
    for day in range(len(hoco_list)):
        print(f"Day {day+1}: {hoco_list[day]}")

    largest("numbers.txt")

def largest(a):
    with open(a) as num_file:
        num_list = num_file.read().splitlines()
    print(max(num_list))
    for i in range(len(num_list)):
        num_list[i]= int(num_list[i])
    print(max(num_list))

if __name__ == "__main__":
    main()
