def display(fr):
    for i in fr:
        print(i, end="\t")
    print()

def optimal_page_replacement(pages, frsize):
    fr,pf = [-1] * frsize ,frsize  
    n = len(pages)
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
            lg = [0] * frsize 
            for i in range(frsize):
                for k in range(j + 1, n):
                    if fr[i] == pages[k]:
                        lg[i] = k - j
                        break
            found = 0
            for i in range(frsize):
                if lg[i] == 0:
                    index = i
                    found = 1
                    break
            if found == 0:
                max_lg = max(lg)
                index = lg.index(max_lg)
            fr[index] = page
            pf += 1
        display(fr)
    print(f"Number of page faults: {pf}")
if __name__ == "__main__":
    n = int(input("Enter no of pages : "))
    pages = [int(input(f"Enter page {i + 1}: ")) for i in range(n)]
    frsize = int(input("Enter the number of frames: "))
    optimal_page_replacement(pages, frsize)
