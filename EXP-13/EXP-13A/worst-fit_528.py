def worst_fit(nb, nf, b, f):
    bf = [0] * nb
    ff = [-1] * nf
    for i in range(nf):
        best_block = max((j for j in range(nb) if bf[j] == 0 and b[j] >= f[i]), key=lambda j: b[j] - f[i], default=-1)
        if best_block != -1:
            bf[best_block] = 1
            ff[i] = best_block
    print("\nFile No\tFile Size\tBlock No\tBlock Size\tFragment")
    for i in range(nf):
        if ff[i] != -1:
            frag = b[ff[i]] - f[i]
            print(f"{i + 1}\t\t{f[i]}\t\t{ff[i] + 1}\t\t{b[ff[i]]}\t\t{frag}")
nb = int(input("Enter the number of blocks: "))
nf = int(input("Enter the number of files: "))
print("\nEnter the size of the blocks:")
b = [int(input(f"Block {i + 1}: ")) for i in range(nb)]
print("Enter the size of the files:")
f = [int(input(f"File {i + 1}: ")) for i in range(nf)]
worst_fit(nb, nf, b, f)
