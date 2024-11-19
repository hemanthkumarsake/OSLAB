class Directory:
    def __init__(self, name):
        self.dname = name
        self.fnames = []  # List to hold file names

    def create_file(self, fname):
        self.fnames.append(fname)

    def delete_file(self, fname):
        if fname in self.fnames:
            self.fnames.remove(fname)
            print(f"File {fname} is deleted")
        else:
            print(f"File {fname} not found")

    def search_file(self, fname):
        if fname in self.fnames:
            print(f"File {fname} is found")
        else:
            print(f"File {fname} not found")

    def display_files(self):
        if not self.fnames:
            print("\nDirectory Empty")
        else:
            print("\nThe Files are -- " + "\t".join(self.fnames))

def main():
    dir_name = input("Enter name of directory -- ")
    directory = Directory(dir_name)

    while True:
        print("\n1. Create File\t2. Delete File\t3. Search File")
        print("4. Display Files\t5. Exit")
        choice = int(input("Enter your choice -- "))

        if choice == 1:
            fname = input("Enter the name of the file -- ")
            directory.create_file(fname)
        elif choice == 2:
            fname = input("Enter the name of the file -- ")
            directory.delete_file(fname)
        elif choice == 3:
            fname = input("Enter the name of the file -- ")
            directory.search_file(fname)
        elif choice == 4:
            directory.display_files()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
