def calculate_times(bt):
    n = len(bt)
    wt, tat = [0] * n, [0] * n
    bt, processes = zip(*sorted(zip(bt, range(n))))
    for i in range(1, n):
        wt[i] = wt[i-1] + bt[i-1]
    for i in range(n):
        tat[i] = wt[i] + bt[i]
    return processes, wt, tat

def main():
    n = int(input("Enter the number of processes -- "))
    bt = [int(input(f"Enter Burst Time for Process {i} -- ")) for i in range(n)]
    processes, wt, tat = calculate_times(bt)
    print("\tPROCESS\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print(f"\tP{processes[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print(f"\nAverage Waiting Time -- {sum(wt)/n:.6f}")
    print(f"Average Turnaround Time -- {sum(tat)/n:.6f}")

if __name__ == "__main__":
    main()
