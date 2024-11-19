def display(fr):
    print("\n", end="")
    for i in fr:
        print(i, end="\t")
    print()
def lru_page_replacement(pages, frsize):
    fr, pf = [-1] * frsize,0
    for j, page in enumerate(pages):
        flag1 = flag2 = 0
        if page in fr:
            flag1 = flag2 = 1
        if flag1 == 0:
            for i in range(frsize):
                if fr[i] == -1:
                    fr[i] = page
                    flag2 = 1
                    break
        if flag2 == 0:
            fs = [0] * frsize
            for k in range(j - 1, -1, -1):
                if pages[k] in fr:
                    fs[fr.index(pages[k])] = 1
                if fs.count(0) == 1:
                    break
            index = fs.index(0)
            fr[index] = page
            pf += 1
        display(fr)
    print(f"\nNo of page faults: {pf + frsize}")
if __name__ == "__main__":
    n = int(input("Enter the number of pages: "))
    pages = [int(input(f"Enter page {i + 1}: ")) for i in range(n)]
    frsize = int(input("Enter frame size: "))
    lru_page_replacement(pages, frsize)
