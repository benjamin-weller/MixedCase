import sys
import pyperclip

def create_string(string, option):
    if option == "lower":
        return string.lower()
    elif option == "mixed":
        return string.title()
    else:
        return string.upper()

if __name__ == "__main__":
    string = pyperclip.paste()
    if len(sys.argv) != 2:
        print("Usage:\nmain.py (lower|mixed|upper)")
    elif string == "":
        print("You must have a string on your clipboard to be changed.")
    else:
        pyperclip.copy(create_string(string, sys.argv[1]))
