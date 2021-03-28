import math
import random
import json
from pathlib import Path

# this is just silly
p = Path(__file__)

WORDS_DIR = p.parent.parent.joinpath('share')

configFile = WORDS_DIR.joinpath('config.json')

jsonObj = open(str(configFile))
jsonData = json.load(jsonObj)

def fisherYates(arr):
    """
    Randomly rearrange an array using Fisher Yates algorithm
    """
    ctn = len(arr)
    for i in range(0, ctn):
        j = math.floor(random.random() * (i + 1))
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    return arr

def scrambleWords(str):
    """
    scramble the characters
    although in python string is also array but it does not
    allow assignment, therefore we still need to turn it into a list
    """
    arr = [ch for ch in str]
    newArr = fisherYates(arr)

    return ''.join(newArr)


def getPossibleWord(str, triedWords):
    """
    get a possible word that we haven't tried before
    """
    possibleWord = scrambleWords(str)
    tempList = [x for x in triedWords if possibleWord in x]
    print(f"triedWords array length: {len(triedWords)}")
    if (len(tempList) > 0):
        return getPossibleWord(str, triedWords)

    return possibleWord


def getWords(dir, name):
    """
    import the words file and turn into a usable format (array)
    """
    filePath = WORDS_DIR.joinpath(jsonData['DOT'].join([str(name), jsonData['FILE_EXT']]))
    fileObj = open(filePath)
    fileContent = fileObj.read()

    return fileContent.strip().split(' ')


def getAnagram(str, words):
    """
    find the anagram from the input str
    """
    dict = [w for w in words if w != str]
    maxTried = math.pow(2, len(str))
    tried = 0
    possibleWords = []

    while tried <= maxTried:
        print(f"Tried number: {tried}")
        word = getPossibleWord(str, possibleWords)
        if (len([w for w in dict if w == word]) > 0):
            return word

        possibleWords.append(word)
        ++tried

    return False
