a1.py is a program that allows the user to list the contents 
of a specified directory on the computer. In order to use the 
program, the command line format is:

[COMMAND] [INPUT] [[-]OPTION] [INPUT]


COMMANDS AND INPUT:
The user may choose between Q, L, C, D, and R for commands. 
L, lists the contents of a directory. Q, quits the program. 
If the command is L, the user must input a path to a directory 
on their local computer. Entering the command will display the 
current files and directories in the specified path. The C 
command creates a new file in the specified directory. The 
user must input the option '-n' after the directory and then the 
name of the file to be created. The file created will be a .dsu 
file. The D command allows the user to delete a file in the provided
directory. You must enter the full path name, with the filename at
the end. The R command reads and prints the contents of a specified 
file. If the file is empty, the program will notify the user. 

OPTIONS:
Along with displaying contents of directories, the user can
make the program display different things. With the option "-r",
the program will display the contents of the specified directory
along with the contents of all subdirectories. The option "-f"
will display only the files in that directory. "-s" allows the
user to search for a specific file. Typing in the name of the file
after the option will search the directory for a path that leads to
the specified file. "-e" will allow the user to search for specific
file formats. For example, if the user types "-e txt" after the path
the program will display all .txt files in that directory. Also,
adding the "-r" option to any of the other options will search in 
all subdirectories as well.
