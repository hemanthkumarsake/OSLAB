def display(fr):
    print("\n", end="")
    for i in fr:
        print(i, end="\t")
    print()
def fifo_page_replacement(pages, frsize):
    fr = [-1] * frsize
    top = 0
    pf = 0
    for page in pages:
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
            fr[top] = page
            top += 1
            pf += 1
            if top >= frsize:
                top = 0
        display(fr)
    print(f"Number of page faults: {pf + frsize}")
if __name__ == "__main__":
    n = int(input("Enter the number of pages: "))
    pages = [int(input(f"Enter page {i + 1}: ")) for i in range(n)]
    frsize = int(input("Enter frame size: "))
    fifo_page_replacement(pages, frsize)
