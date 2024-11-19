def scan_disk_scheduling(tracks, head_position):
    # Sort the tracks
    tracks.sort()

    # Find the position of the head in the sorted list
    head_index = 0
    for i in range(len(tracks)):
        if tracks[i] >= head_position:
            head_index = i
            break

    # Decide the order of traversal based on SCAN algorithm
    left = tracks[:head_index][::-1]  # Tracks to the left of the head, reversed
    right = tracks[head_index:]       # Tracks to the right of the head

    # Traverse to the right first, then to the left (simulating a rightward scan)
    seek_sequence = right + left

    # Calculate the differences between each pair of consecutive tracks
    differences = []
    current_position = head_position
    for track in seek_sequence:
        difference = abs(track - current_position)
        differences.append(difference)
        current_position = track

    # Calculate total and average header movements
    total_movements = sum(differences)
    average_movements = total_movements / len(differences)

    # Display the results
    print("Tracks traversed")
    for track in seek_sequence:
        print(track)

    print("\nDifference between tracks")
    for difference in differences:
        print(difference)

    print(f"\nAverage header movements: {average_movements:.2f}")


# Input
n = int(input("Enter the number of tracks: "))
print("Enter track positions:")
tracks = list(map(int, input().split()))
head_position = int(input("Enter the position of the head: "))

# Run the SCAN disk scheduling algorithm
scan_disk_scheduling(tracks, head_position)
