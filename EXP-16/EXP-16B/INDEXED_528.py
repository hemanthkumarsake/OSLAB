def indexed_file_allocation():
    f = [0] * 50
    while True:
        p = int(input("Enter index block: "))
        if f[p] == 0:
            f[p] = 1
            n = int(input("Enter number of files on index: "))
            inde = [int(input()) for i in range(n)]
            if all(f[i] == 0 for i in inde):
                for j in inde:
                    f[j] = 1 
                print("\nAllocated")
                print("File indexed:")
                for k in inde:
                    print(f"{p}->{k}:{f[k]}")
            else:
                print("One or more blocks are already allocated.")
        else:
            print("Index block already allocated.")
        if int(input("Enter 1 to enter more files and 0 to exit: ")) == 0:
            break
indexed_file_allocation()
