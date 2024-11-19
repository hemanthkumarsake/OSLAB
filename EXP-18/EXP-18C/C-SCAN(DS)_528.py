def main():
    # Input values
    tracks = list(map(int, input("Enter the track positions (separated by spaces): ").split()))
    head_position = int(input("Enter starting position: "))
    total_tracks = max(tracks) + 1  # Assuming total track range from 0 to max track + 1 for the edge case

    # Adding edge values and the head position
    tracks.extend([0, total_tracks - 1, head_position])
    tracks = sorted(tracks)

    # Finding the position of the head in the sorted list
    head_index = tracks.index(head_position)

    # Organizing the tracks in C-SCAN order
    # Move right to the end, then start from the beginning till the head position
    ordered_tracks = tracks[head_index:] + tracks[:head_index]

    # Calculating the differences and total movements
    differences = []
    total_movement = 0

    for i in range(1, len(ordered_tracks)):
        difference = abs(ordered_tracks[i] - ordered_tracks[i - 1])
        differences.append(difference)
        total_movement += difference

    # Output results
    print("\nOUTPUT")
    print("Tracks traversed\tDifference Between tracks")
    for i in range(1, len(ordered_tracks)):
        print(f"{ordered_tracks[i]}\t\t\t{differences[i - 1]}")

    # Average seek time
    avg_seek_time = total_movement / (len(tracks) - 3)  # excluding added 0, max track, and head position
    print(f"\nAverage seek time: {avg_seek_time:.8f}")

if __name__ == "__main__":
    main()
