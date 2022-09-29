#!/usr/bin/python3

import sys
import subprocess

# binary path
xclip = "/usr/bin/xclip"

# copy / paste
mode = ""
# file name
file_name = ""
# file type
file_type = ""
# list of all pre-set file type
file_type_list = ["image/png", "image/jpeg", "image/tiff"]

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout

def run_command_text(command):
    return run_command(command).decode("utf-8")

def get_argument(index):
    return sys.argv[index]

def select_mode():
    global mode
    while True:
        i = input("Please select mode (copy/paste) > ").lower()
        if i == "c" or i == "copy":
            mode = "copy"
            break;
        elif i == "p" or i == "paste":
            mode = "paste"
            break;
        else:
            print("Invalid value.")

def select_file_name():
    global file_name
    while True:
        i = input("Please enter file name > ")
        print("Your file name is \"" + i + "\". Confirm? [y/n] ", end="")
        c = input().lower()
        if c == "y" or c == "yes":
            file_name = i
            break

def select_file_type():
    global file_type
    while True:
        print("Please enter file type")
        print("0) Custom")
        index = 1
        map = {}
        for l in file_type_list:
            print(f"{index}) {l}")
            map[index] = l
            index += 1
        i = input("> ")
        try:
            i = int(i)
        except ValueError:
            print("Invalid option.")
            continue
        if i > index or i < 0:
            print("Invalid option.")
            continue
        elif i == 0:
            f = input("Please enter custom file type > ")
            file_type = f
            break
        try:
            f = map[i]
            file_type = f
            break
        except KeyError:
            f = input("Error!")
            continue

# TODO: Fix this thing
def copy():
    command = [xclip, "-selection", "clipboard", file_name]
    return run_command_text(command=command)

def paste():
    command = [xclip, "-selection" "clipboard", "-target", file_type, "-out"]
    return run_command(command=command)

def main():
    select_mode()
    select_file_name()
    if mode == "copy":
        text = copy()
        # empty text but ...
        print(text)
    elif mode == "paste":
        select_file_type()
        byte = paste()
        with open(file_name, "wb") as bin:
            bin.write(byte)
    else:
        print("What mode is this??")
        sys.exit(-1)

if __name__ == "__main__":
    main()
