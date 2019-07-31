import sys
import pyperclip

def create_mixed_word(word):
    start_char = word[:1]
    remainder = word[1:]
    return start_char.upper() + remainder.lower()

def create_mixed_phrase(phrase):
    returned = ""
    for x in phrase.split(" "):
        returned += create_mixed_word(x) + " "
    return returned.strip()

def create_string(string, option):
    if option == "lower":
        return string.lower()
    elif option == "mixed":
        return create_mixed_phrase(string)
    else:
        return string.upper()

if __name__ == "__main__":
    string = pyperclip.paste()
    if len(sys.argv) != 2:
        print("Usage:\nmain.py (lower|mixed|upper)")
    elif string == "":
        print("You must have a string on your clipboard to be changed.")

    pyperclip.copy(create_string(string, sys.argv[1]))
