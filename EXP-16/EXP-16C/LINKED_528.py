def main():
    f = [0] * 50  # Array to represent the file allocation status (50 blocks)
    
    # Get the number of already allocated blocks
    p = int(input("Enter how many blocks that are already allocated: "))
    
    print("\nEnter the block numbers that are already allocated:")
    for _ in range(p):
        a = int(input())
        f[a] = 1  # Mark the block as allocated
    
    while True:
        # Get the starting block and length
        st = int(input("\nEnter the starting index block: "))
        length = int(input("Enter the length: "))
        
        k = length
        for j in range(st, st + k):
            if f[j] == 0:  # If the block is free
                f[j] = 1  # Allocate the block
                print(f"\n{j} -> Allocated")
            else:  # If the block is already allocated
                print(f"\n{j} -> Block is already allocated")
                k += 1  # Extend the length to find an alternative block
        
        # Ask if the user wants to allocate another file
        c = int(input("\nDo you want to enter one more file? (yes-1/no-0): "))
        if c == 0:
            break


if __name__ == "__main__":
    main()
