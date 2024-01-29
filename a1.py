# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Lex Ibanez
# laibanez@uci.edu
# 70063614

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
        print("ERROR")
        return
    if "-n" in options:
        index = options.index('-n')
        if index + 1 < len(options):
            file_name = options[index + 1]
            new_path = directory / f'{file_name}.dsu'
            new_path.touch()
            print(new_path)
        else:
            print("ERROR")
    else:
        print("ERROR")


def delete_file(directory):
    if directory.is_file():
        if directory.suffix == '.dsu':
            file_name = directory
            directory.unlink()
            print(f'{file_name} DELETED')
        else:
            print("ERROR")
    else:
        print("ERROR")


def read_file(directory):
    if directory.is_file():
        if directory.suffix == '.dsu':
            with open(directory, 'r') as file:
                content = file.read()
                if not content:
                    print("EMPTY")
                else:
                    print(content.strip())
        else:
            print("ERROR")
    else:
        print("ERROR")


def main():
    while True:
        user_input = input()
        command, *args = user_input.split()
        
        if command.lower() == 'q':
            break

        options = []
        if len(args) > 1:
            options = args
        if args:
            directory = Path(args[0])

        
        if command.lower() == 'l': 
            if directory.is_dir():
                list_directory(directory, options)
            else:
                print('Could not find directory.')
        elif command.lower() == 'c':
            try:
                create_file(directory, options)
            except UnboundLocalError:
                print("ERROR")
        elif command.lower() == 'd':
            delete_file(directory)
        elif command.lower() == 'r':
            read_file(directory)
        else:
            print("Invalid command.")
            continue

        
if __name__ == '__main__':
    main()