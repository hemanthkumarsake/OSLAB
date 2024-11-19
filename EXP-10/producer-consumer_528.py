def main():
    buffer = [0] * 10
    bufsize, in_index, out_index = 10, 0, 0

    while True:
        choice = int(input("\n1. Produce\t2. Consume\t3. Exit\nEnter your choice: "))
        if choice == 1:
            if (in_index + 1) % bufsize == out_index:
                print("Buffer is Full")
            else:
                buffer[in_index] = int(input("Enter the value: "))
                in_index = (in_index + 1) % bufsize
        elif choice == 2:
            if in_index == out_index:
                print("Buffer is Empty")
            else:
                print(f"The consumed value is {buffer[out_index]}")
                out_index = (out_index + 1) % bufsize
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
