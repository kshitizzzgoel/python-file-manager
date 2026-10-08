
import os

while True:
    print('press 1 for creating a file')
    print('press 2 for updating a file')
    print('press 3 for reading a file')
    print('press 4 for deleting a file')
    print('press 5 for exiting the current file handling process')

    try:
        check = int(input("press ur preference = "))
    except Exception as err:
        print(f"error in ur input {err}")
        continue

    if check == 1:
        filename = input("enter ur file name-")
        file = open(f"{filename}.txt", "w")
        file.close()
        print(f'ur file is created {filename}.txt')
    elif check == 2:
        filename = input("enter ur file name-")
        try:
            file = open(f"{filename}.txt", "r+")
            file.seek(0, 2)
            content = input("enter the content u want to add - ")
            file.write(content + "\n")
            file.close()
            print("congo ur file has been updated")
        except Exception as arr:
            print(f'error {arr}')
    elif check == 3:
        filename = input("enter ur file name-")
        try:
            file = open(f"{filename}.txt", "r")
            mine = file.read()
            file.close()
            print(f"file content --- {mine}-------")
        except FileNotFoundError:
            print("ur file doesn't exist on the pc")
    elif check == 4:
        filename = input("enter ur file name-")
        try:
            os.remove(f"{filename}.txt")
            print(f"ur file {filename}.txt has been deleted")
        except FileNotFoundError:
            print("ur file doesn't exist on the pc")
    elif check == 5:
        print("program ended")
        break
    else:
        print("invalid preference")