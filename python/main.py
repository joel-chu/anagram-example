#!/usr/bin/env python

from anagram import main

# make this more interactive

def run():
    """
    Wrap the interactive version in one
    """
    print("Type quit() or press CTRL-C to exit")
    while (True):
        print("Please give a word between 2~15 characters long")
        word = input("> ")
        if (word == "quit()"):
            exit(0)
        else:
            main(word)
            print("-" * 20)


run()

