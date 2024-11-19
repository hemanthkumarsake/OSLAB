def file_allocation():
    f = [0] * 50
    while True:
        st = int(input("Enter the starting block: "))
        length = int(input("Enter the length of the file: "))
        for j in range(st, st + length):
            if f[j] == 0:
                f[j] = 1
                print(f"{j}->1")
            else:
                print(f"Block {j} already allocated")
                break
        else:
            print("The file is allocated to disk.")
        if int(input("Enter more files? (1-Yes/0-No): ")) == 0:
            break
file_allocation()
