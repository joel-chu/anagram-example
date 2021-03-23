from sys import argv

from mylib import jsonData, getWords, getAnagram

WORDS_DIR = '../share'

def anagram(str):
    """
    The main method to get the anagram
    """
    l = len(str)
    if l > jsonData['MAX_CHAR'] || l < jsonData['MIN_CHAR']:
        print(f"Error: please provide a word between {jsonData['MIN_CHAR']} and {jsonData['MAX_CHAR']}")
    else:
        words = getWords(WORDS_DIR, l)
        return getAnagram(str, words)



if __name__ == '__main__':
    script, word = argv
    result = anagram(word)
    if result:
        print(f"We found the angram for {word} > {result}")
    else:
        print("Sorry could not find anything")
