def one(howhung, hu, philname):
    print("\nAllow one philosopher to eat at any time\n")
    for i in range(howhung):
        print(f"\nP {philname[hu[i]]} is granted to eat")
        for x in range(i + 1, howhung):
            print(f"P {philname[hu[x]]} is waiting")
def two(howhung, hu, philname):
    print("\nAllow two philosophers to eat at the same time\n")
    s = 0
    for i in range(howhung):
        for j in range(i + 1, howhung):
            if abs(hu[i] - hu[j]) >= 1 and abs(hu[i] - hu[j]) != 4:
                s += 1
                print(f"\n\nCombination {s}")
                t = hu[i]
                r = hu[j]
                print(f"\nP {philname[t]} and P {philname[r]} are granted to eat")
                for x in range(howhung):
                    if hu[x] != t and hu[x] != r:
                        print(f"P {philname[hu[x]]} is waiting")
def main():
    print("\n\nDINING PHILOSOPHER PROBLEM")
    tph = int(input("Enter the total number of philosophers: "))
    
    philname = [i + 1 for i in range(tph)]
    status = [1 for _ in range(tph)]
    
    howhung = int(input("How many are hungry: "))
    
    if howhung == tph:
        print("\nAll are hungry..\nDeadlock stage will occur")
        print("Exiting")
        return
    hu = []
    for i in range(howhung):
        pos = int(input(f"Enter philosopher {i + 1} position: ")) - 1
        hu.append(pos)
        status[pos] = 2
    while True:
        print("\n1. One can eat at a time")
        print("2. Two can eat at a time")
        print("3. Exit")
        cho = int(input("Enter your choice: "))
        if cho == 1:
            one(howhung, hu, philname)
        elif cho == 2:
            two(howhung, hu, philname)
        elif cho == 3:
            print("Exiting program.")
            break
        else:
            print("\nInvalid option..")
if __name__ == "__main__":
    main()
