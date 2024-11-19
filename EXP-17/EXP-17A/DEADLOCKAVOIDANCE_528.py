def main():
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resources: "))

    alloc = [[0] * m for _ in range(n)]  # Allocation matrix
    max_claim = [[0] * m for _ in range(n)]  # Maximum claim matrix
    total = [0] * m  # Total available resources
    work = [0] * m  # Work vector
    need = [[0] * m for _ in range(n)]  # Need matrix
    finish = ['n'] * n  # Finish flags for processes

    # Input the claim matrix
    print("Enter the claim matrix:")
    for i in range(n):
        max_claim[i] = list(map(int, input().split()))

    # Input the allocation matrix
    print("Enter the allocation matrix:")
    for i in range(n):
        alloc[i] = list(map(int, input().split()))

    # Input the total resource vector
    print("Enter the resource vector:")
    total = list(map(int, input().split()))

    # Calculate available resources
    avail = [0] * m
    for j in range(m):
        avail[j] = sum(alloc[i][j] for i in range(n))
    
    # Calculate the initial work vector
    for j in range(m):
        work[j] = total[j] - avail[j]

    # Calculate the need matrix
    for i in range(n):
        for j in range(m):
            need[i][j] = max_claim[i][j] - alloc[i][j]

    count = 0

    while count < n:
        safe = False
        for i in range(n):
            if finish[i] == 'n':  # Check if the process is not yet finished
                if all(need[i][j] <= work[j] for j in range(m)):  # Check resource availability
                    print(f"\nAll the resources can be allocated to Process {i + 1}")
                    for j in range(m):
                        work[j] += alloc[i][j]
                    finish[i] = 'y'
                    safe = True
                    count += 1
                    print(f"Available resources after allocating to Process {i + 1}: {work}")
                    print(f"Process {i + 1} executed?: {finish[i]}")
                    break
        if not safe:
            print("\nSystem is not in a safe state!")
            return

    print("\nSystem is in a safe mode")
    print("The given state is a safe state")


if __name__ == "__main__":
    main()
