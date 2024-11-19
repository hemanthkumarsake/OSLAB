def first_fit(nb, nf, b, f):
    bf, frag = [0] * nb, [0] * nf
    for i in range(nf):
        for j in range(nb):
            if not bf[j] and b[j] >= f[i]:
                frag[i], bf[j] = b[j] - f[i], 1
                print(f"{i+1}\t\t{f[i]}\t\t{j+1}\t\t{b[j]}\t\t{frag[i]}")
                break

nb, nf = int(input("Enter number of blocks: ")), int(input("Enter number of files: "))

print("\nEnter the size of the blocks:")
b = [int(input(f"Block {i+1}: ")) for i in range(nb)]

print("Enter the size of the files:")
f = [int(input(f"File {i+1}: ")) for i in range(nf)]

print("\nFile_no\tFile_size\tBlock_no\tBlock_size\tFragment")
first_fit(nb, nf, b, f)
