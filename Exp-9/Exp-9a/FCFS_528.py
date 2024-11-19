def calculate_times(bt):
    n, wt, tat = len(bt), [0] * len(bt), [0] * len(bt)
    for i in range(1, n):
        wt[i] = wt[i-1] + bt[i-1]
    for i in range(n):
        tat[i] = wt[i] + bt[i]
    return wt, tat

def main():
    n = int(input("Enter the number of processes -- "))
    bt = [int(input(f"Enter Burst Time for Process {i} -- ")) for i in range(n)]
    wt, tat = calculate_times(bt)
    print("\tPROCESS\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
    for i in range(len(bt)):
        print(f"\tP{i}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print(f"\nAverage Waiting Time -- {sum(wt)/len(bt):.6f}")
    print(f"Average Turnaround Time -- {sum(tat)/len(bt):.6f}")

if __name__ == "__main__":
    main()
 
