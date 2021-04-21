import sys
import json


from functools import reduce
from pathlib import Path

from mymathlib import getTotalCombinationNum
from mywordlib import scrambleWords

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

# decorator import (note we need to explictly name the import)
# from mydeco import timer_decorator

# Functions

def getWords(dir, name):
    """
    import the words file and turn into usable format (array)
    """
    filePath = WORDS_DIR.joinpath(jsonData['DOT'].join([str(name), jsonData['FILE_EXT']]))
    fileObj = open(filePath)
    fileContent = fileObj.read()

    return fileContent.strip().split(' ')


def getPossibleWord(str, triedWords, combTotal, recursionLimit, totalTry = 0):
    """
    We need to get around that maxium recursionError
    """
    result = getPossibleWordInner(str, triedWords, recursionLimit)
    totalTry += result[1] # this is the i
    word = result[0]
    if (word == False): # which means it ended at the recursionLimit
        return getPossibleWordInner(str, triedWords)
    else:
        return (word, totalTry)


def getPossibleWordInner(str, triedWords, maxAllowTry, i = 0):
    """
    get a possible word that we haven't tried before
    @BUG if this recursion run over 1000 (997 in fact) times,
    it will throw RecursionError
    because it reaches the system maximum
    """
    # if this interaction has reach the max allow number
    # we just terminate it and try in the next loop
    if (i >= maxAllowTry):
        return (False, i)
    i += 1
    # continue with guessing a word
    possibleWord = scrambleWords(str)
    # if its already tried then run itself again
    if (possibleWord in triedWords):
        return getPossibleWord(str, triedWords, maxAllowTry, i)

    return (possibleWord, i)

# need to decorator the function when we declare the function
# something fucks up, it crash the function when using decorator
# Error: TypeError: 'NoneType' object is not callable
# @timer_decorator
def getAnagram(str, words):
    """
    find the anagram from the input str
    V.2 with small changes to get around the recursion limit
    """
    # first we check if this word is in the dict first
    # otherwise there is no point of running the follow code
    exist = str in words
    if (not exist):
        return (False, 0, 0) # the problem is here
    # filter out the provided word
    dict = [w for w in words if w != str]
    totalCombinationNum = getTotalCombinationNum(len(str))
    guessTotal = 0
    tried = 0
    possibleWords = []
    # V.2 we move the while loop into the getPossibleWord
    # because we need to check the maximum allow loop in each call
    while tried <= totalCombinationNum:
        # print(f"Tried number: {tried}")
        # V.2 we add maxTry parameter
        result = getPossibleWord(str, possibleWords, totalCombinationNum, recursionLimit)
        word = result[0]
        guessTotal += result[1]
        if (word in dict):
            return (word, tried, guessTotal)
        # if the word is False that just terminate because it reaches the maxTry
        # we don't count that as one try
        if (word):
            possibleWords.append(word)
            tried += 1

    return (False, tried, guessTotal) # couldn't find anything that should be impossible
