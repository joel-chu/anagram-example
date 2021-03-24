from sys import argv

from mylib import WORDS_DIR, jsonData, getWords, getAnagram

def anagram(str):
    """
    The main method to get the anagram
    """
    l = len(str)
    if l > jsonData['MAX_CHAR'] or l < jsonData['MIN_CHAR']:
        print(f"Error: please provide a word between {jsonData['MIN_CHAR']} and {jsonData['MAX_CHAR']}")
    else:

        words = getWords(WORDS_DIR, l)
        return getAnagram(str, words)

def main(word):
    result = anagram(word)
    if result:
        print(f"We found an angram for {word} > {result}")
    else:
        print("Sorry could not find anything")


if __name__ == '__main__':
    script, word = argv
    main(word)
