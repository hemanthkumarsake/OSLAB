def priority_scheduling():
    n = int(input("Enter the number of processes: "))
    processes = [list(map(int, input(f"Enter Burst Time and Priority of Process {i} (separated by space): ").split())) + [i] for i in range(n)]
    processes.sort(key=lambda x: x[1])
    wt, tat = [0] * n, [0] * n
    wtavg = tatavg = 0
    for i in range(n):
        if i > 0:
            wt[i] = wt[i-1] + processes[i-1][0]
        tat[i] = wt[i] + processes[i][0]
        wtavg += wt[i]
        tatavg += tat[i]
    print("\nPROCESS\tPRIORITY\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print(f"{processes[i][2]}\t{processes[i][1]}\t\t{processes[i][0]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage Waiting Time is --- {wtavg/n:.6f}")
    print(f"Average Turnaround Time is --- {tatavg/n:.6f}")

if __name__ == "__main__":
    priority_scheduling()
