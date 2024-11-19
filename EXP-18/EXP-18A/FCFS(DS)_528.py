def main():
    # Initialize variables
    t = []
    tohm = []
    tot = 0

    # Get the number of tracks
    n = int(input("Enter the number of tracks: "))

    # Get the tracks to be traversed
    print("Enter the tracks to be traversed:")
    for i in range(n):
        track = int(input())
        t.append(track)

    # Calculate the difference between consecutive tracks
    for i in range(n - 1):
        difference = abs(t[i + 1] - t[i])
        tohm.append(difference)

    # Calculate the total and average header movements
    tot = sum(tohm)
    avhm = tot / n

    # Print the results
    print("Tracks traversed\tDifference between tracks")
    for i in range(n - 1):
        print(f"{t[i + 1]}\t\t{tohm[i]}")
    print(f"\nAverage header movements: {avhm:.2f}")

# Run the main function
main()
