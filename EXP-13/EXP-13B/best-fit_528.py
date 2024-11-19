def best_fit(nb, nf, b, f):
    bf = [0] * nb
    for i in range(nf):
        best_block, lowest = -1, float('inf')
        for j in range(nb):
            if not bf[j] and 0 <= (b[j] - f[i]) < lowest:
                best_block, lowest = j, b[j] - f[i]
        if best_block != -1:
            bf[best_block] = 1
            print(f"{i+1}\t\t{f[i]}\t\t{best_block+1}\t\t{b[best_block]}\t\t{lowest}")
nb = int(input("Enter number of blocks: "))
nf = int(input("Enter number of files: "))
print("\nEnter the size of the blocks:")
b = [int(input(f"Block {i+1}: ")) for i in range(nb)]
print("Enter the size of the files:")
f = [int(input(f"File {i+1}: ")) for i in range(nf)]
print("\nFile No\tFile Size\tBlock No\tBlock Size\tFragment")
best_fit(nb, nf, b, f)
