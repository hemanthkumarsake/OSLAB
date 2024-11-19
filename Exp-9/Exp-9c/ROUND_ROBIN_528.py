def round_robin():
    n = int(input("Enter the number of processes: "))
    bt = [int(input(f"Enter Burst Time for process {i + 1}: ")) for i in range(n)]
    ct = bt.copy()
    t = int(input("Enter the size of the time slice: "))
    tat = [0] * n
    temp = 0
    while any(b > 0 for b in bt):
        for i in range(n):
            if bt[i] > 0:
                if bt[i] <= t:
                    temp += bt[i]
                    tat[i] = temp
                    bt[i] = 0
                else:
                    bt[i] -= t
                    temp += t
    wt = [tat[i] - ct[i] for i in range(n)]
    print("\n\tPROCESS\t BURST TIME \t WAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print(f"\t{i + 1} \t {ct[i]} \t\t {wt[i]} \t\t {tat[i]}")
    print(f"\nThe Average Turnaround time is -- {(sum(tat) / n):.6f}")
    print(f"The Average Waiting time is -- {(sum(wt) / n):.6f}")
if __name__ == "__main__":
    round_robin()
