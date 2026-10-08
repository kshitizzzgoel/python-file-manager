# Python File Management System

A simple **Python-based file management system** that allows users to create, update, read, and delete text files through a command-line interface.

## Features

- Create a new `.txt` file
- Add/update content in an existing file
- Read the contents of a file
- Delete a file
- Handles files that don't exist
- Runs continuously until the user chooses to exit
- Handles invalid menu input

## Technologies Used

- Python
- `os` module
- File Handling
- Exception Handling
- `while` loop

## How It Works

When the program starts, it displays a menu:

```text
1. Create a file
2. Update a file
3. Read a file
4. Delete a file
5. Exit
```

The user selects an option and provides the file name when required.

### File Modes Used

- `"w"` → Creates a new file or overwrites an existing file
- `"r+"` → Opens an existing file for reading and writing
- `"r"` → Opens a file for reading

The program also uses:

```python
os.remove()
```

to delete files.

## Example

```text
press 1 for creating a file
press 2 for updating a file
press 3 for reading a file
press 4 for deleting a file
press 5 for exiting the current file handling process

press ur preference = 1
enter ur file name- notes

ur file notes.txt is created
```

You can then choose option `2` to add content, option `3` to read the file, or option `4` to delete it.

## What I Learned

Through this project, I practiced:

- Python file handling
- `open()`
- `read()`
- `write()`
- `seek()`
- `close()`
- `try` and `except`
- `FileNotFoundError`
- `while` loops
- `break` and `continue`
- The `os` module

## Future Improvements

Some improvements I may add in the future:

- Rename files
- Search for files
- Display all available files
- Add a graphical user interface
- Add better input validation
- Use functions to make the code cleaner

## Author

**Kshitiz Goel**

This is a beginner Python project created to practice file handling and basic Python concepts.
