import sys
import math
import random
import json
from pathlib import Path
# prepare the configuration data
p = Path(__file__)
WORDS_DIR = p.parent.parent.joinpath('share')
configFile = WORDS_DIR.joinpath('config.json')

jsonObj = open(str(configFile))
jsonData = json.load(jsonObj)
# Get the number of maximum recursion calls
# we only use 90% of what its allow on the safe side
# in fact the number is not accurate, system report 1000 but the
# recursion stop at 997
recursionLimit = sys.getrecursionlimit() * 0.9

# Functions

def getWords(dir, name):
    """
    import the words file and turn into usable format (array)
    """
    filePath = WORDS_DIR.joinpath(jsonData['DOT'].join([str(name), jsonData['FILE_EXT']]))
    fileObj = open(filePath)
    fileContent = fileObj.read()

    return fileContent.strip().split(' ')

def getMaxTryNum(n, total = 0):
    """
    The old calculation was wrong, we need the total possible combination number
    which is Xn ... X2 * X1 = total
    """
    if (n == 1):
        return total
    if (total == 0):
        total = n
    n -= 1
    total *= n
    return getMaxTryNum(n, total)


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
    using comprehension
    """
    arr = [ch for ch in str]
    newArr = fisherYates(arr)

    return ''.join(newArr)


def getPossibleWord(str, triedWords, maxAllowTry, i = 0):
    """
    get a possible word that we haven't tried before
    @BUG if this recursion run over 1000 (997 in fact) times,
    it will throw RecursionError
    because it reaches the system maximum
    """
    # if this interaction has reach the max allow number
    # we just terminate it and try in the next loop
    if (i >= maxAllowTry):
        return False
    i += 1
    # continue with guessing a word
    possibleWord = scrambleWords(str)
    # if its already tried then run itself again
    if (possibleWord in triedWords):
        return getPossibleWord(str, triedWords, maxAllowTry, i)

    return possibleWord

def getAnagram(str, words):
    """
    find the anagram from the input str
    V.2 with small changes to get around the recursion limit
    """
    # first we check if this word is in the dict first
    # otherwise there is no point of running the follow code
    exist = str in words
    if (not exist):
        return exist
    # filter out the provided word
    dict = [w for w in words if w != str]
    maxTried = getMaxTryNum(len(str))
    tried = 0
    possibleWords = []
    # V.2 we move the while loop into the getPossibleWord
    # because we need to check the maximum allow loop in each call
    while tried <= maxTried:
        # print(f"Tried number: {tried}")
        # V.2 we add maxTry parameter
        word = getPossibleWord(str, possibleWords, recursionLimit)
        if (word in dict):
            return word
        # if the word is False that just terminate because it reaches the maxTry
        # we don't count that as one try
        if (word):
            possibleWords.append(word)
            ++tried

    return False
