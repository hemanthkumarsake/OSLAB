class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def create_file(self, fname):
        self.files.append(fname)

    def delete_file(self, fname):
        if fname in self.files:
            self.files.remove(fname)
            return f"File {fname} deleted."
        return f"File {fname} not found."

    def search_file(self, fname):
        return f"File {fname} is {'found' if fname in self.files else 'not found'}."


class FileSystem:
    def __init__(self):
        self.directories = {}

    def create_directory(self, dname):
        self.directories[dname] = Directory(dname)
        return "Directory created."

    def get_directory(self, dname):
        return self.directories.get(dname)

    def display(self):
        if not self.directories:
            return "No directories."
        return "Directory\tFiles\n" + "\n".join(
            f"{dir.name}\t\t{'\t'.join(dir.files)}" for dir in self.directories.values()
        )


def main():
    fs = FileSystem()
    while True:
        choice = int(input("\n1. Create Directory\t2. Create File\t3. Delete File\n"
                           "4. Search File\t\t5. Display\t6. Exit\nEnter your choice -- "))
        if choice == 1:
            dname = input("Enter name of directory -- ")
            print(fs.create_directory(dname))
        elif choice in [2, 3, 4]:
            dname = input("Enter name of the directory -- ")
            dir = fs.get_directory(dname)
            if dir:
                fname = input("Enter name of the file -- ")
                if choice == 2:
                    dir.create_file(fname)
                    print("File created.")
                elif choice == 3:
                    print(dir.delete_file(fname))
                else:
                    print(dir.search_file(fname))
            else:
                print(f"Directory {dname} not found.")
        elif choice == 5:
            print(fs.display())
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
