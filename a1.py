from pathlib import Path

# test path
# C:\Users\lexib\OneDrive\Desktop\test

def list_directory(directory, options):
    contents = list(directory.iterdir())

    files = [x for x in contents if x.is_file()] # sort contents for files
    directories = [x for x in contents if x.is_dir()] # sort contents for directories

    if '-e' in options:
        if len(options) == 3:
            suffix = options[2] # gets the suffix to be searched
        elif len(options) == 4:
            suffix = options[3] # gets the suffix to be searched
    
        for file in files:
            if file.suffix == '.' + suffix:
                print(file)
        for directory in directories:
            if '-r' in options:
                list_directory(directory, options)

    elif '-s' in options:
        if len(options) == 3:
            search_file = options[2] # gets the file to be searched
        elif len(options) == 4:
            search_file = options[3] # gets the file to be searched

        if Path(directory / search_file).is_file(): # checks if the search file has a path
            print(Path(directory / search_file))
        for directory in directories:
            if '-r' in options:
                list_directory(directory, options)

    elif '-f' in options:
        for file in files:
            print(file)
        for directory in directories:
            if '-r' in options:
                list_directory(directory, options)

    else:
        for file in files:
            print(file)
        for directory in directories:
            print(directory)
            if '-r' in options:
                list_directory(directory, options)

def create_file(directory, options):
    if not directory.is_dir():
        print("Path is not a directory.")
        return
    if "-n" in options:
        index = options.index('-n')
        if index + 1 < len(options):
            file_name = options[index + 1]
            new_path = directory / f'{file_name}.dsu'
            new_path.touch()
            print(new_path)
        else:
            print("No file name provided.")
    else:
        print("Option -n not provided.")

def delete_file(directory):
    if directory.is_file():
        if directory.suffix == '.dsu':
            file_name = directory
            directory.unlink()
            print(f'{file_name} DELETED')
        else:
            print("File is not a .dsu file.")
    else:
        print("File does not exist.")



def main():
    while True:
        user_input = input("Enter Command: ")
        command, *args = user_input.split()
        options = []
        if len(args) > 1:
            options = args
        if args:
            directory = Path(args[0])

        if command.lower() == 'q':
            break
        elif command.lower() == 'l': 
            if directory.is_dir():
                list_directory(directory, options)
            else:
                print('Could not find directory.')
        elif command.lower() == 'c':
            create_file(directory, options)
        elif command.lower() == 'd':
            delete_file(directory)
        elif command.lower() == 'r':
            pass
        else:
            print("Invalid command.")
            continue

        
if __name__ == '__main__':
    main()