#!/usr/bin/env python3

from anagram import main, jsonData


# make this interactive

def run():
    """
    Wrap the interactive version in one
    """
    print("Type quit() or press CTRL-C to exit")
    while (True):
        print(f"Please give a word between {jsonData['MIN_CHAR']}~{jsonData['MAX_CHAR']} characters long")
        word = input("> ")
        if (word == "quit()"):
            exit(0)
        else:

            main(word)
            print("-" * 20)
    return True



run()
