def main():
    # Input number of jobs
    n = int(input("Enter the number of jobs: "))

    # Initialize job names and times
    jobs = []
    times = []

    for i in range(n):
        job_name = input(f"Enter name of job {i + 1}: ")
        time = int(input(f"Enter time for job {i + 1}: "))
        jobs.append(job_name)
        times.append(time)

    # Input available resources
    avail = int(input("Enter the available resources: "))

    # Create temporary lists for sorting
    temp = times.copy()
    indices = list(range(n))

    # Sort jobs based on their execution time
    for i in range(n):
        for j in range(i + 1, n):
            if temp[i] > temp[j]:
                # Swap times
                temp[i], temp[j] = temp[j], temp[i]
                # Swap indices
                indices[i], indices[j] = indices[j], indices[i]

    # Find safe sequence
    safe_sequence = []
    for i in range(n):
        job_index = indices[i]
        if times[job_index] <= avail:
            safe_sequence.append(job_index)
            avail -= times[job_index]
            print(f"{jobs[job_index]}")
        else:
            print("No safe sequence")
            break

    # Print the safe sequence
    if safe_sequence:
        print("Safe sequence is:")
        for index in safe_sequence:
            print(f"{jobs[index]} {times[index]}")

if __name__ == "__main__":
    main()
