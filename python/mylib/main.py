import sys
import json
import time
import random
import math

from functools import reduce
from pathlib import Path

from mylib.algo import getTotalCombinationNum
from mylib.word import scrambleWords

# prepare the configuration data
p = Path(__file__)
# @TODO this is getting really silly need to pass this via a param
WORDS_DIR = p.parent.parent.parent.joinpath('share')
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

def getCharSeq(word):
    """
    input the possible world and sort the character by A-Z
    """
    seq = [ch for ch in word]
    seq.sort()

    return ''.join(seq)

def getMinuteSecond(seconds):
    minute = math.floor(seconds/60)
    secondsLeft = seconds - minute*60
    # getting too long and ugly so break it down
    msg = f"{minute} minute{'s' if minute > 1 else ''}"
    if (secondsLeft > 0):
        msg += f" {secondsLeft} second{'s' if secondsLeft > 1 else ''}"
    return msg

def countDownMsg(seconds, msg=""):
    for c in range(seconds, 0, -1):
        print(f"{msg}run again in {getMinuteSecond(c)}", end="\r")
        time.sleep(1)

def getDuration(s):
    """
    return how many days / hours / minutes / seconds
    """
    days = 0
    hrs = 0
    mins = math.floor(s/60)
    secs = s - mins * 60
    if (mins > 60): # over an hour
        hrs = math.floor(mins/60)
        mins = mins - hrs * 60
        if (hrs > 24): # over a day
            days = math.floor(hrs/24)
            hrs = hrs - days * 24
    return (days, hrs, mins, secs)

def getFormatDuration(s):
    days, hrs, mins, secs = getDuration(s)
    msg = []
    if (days > 0):
        msg.append(f"{days} day{'s' if days > 1 else ''}")
    if (hrs > 0):
        msg.append(f"{hrs} hour{'s' if hrs > 1 else ''}")
    if (mins > 0):
        msg.append(f"{mins} minute{'s' if mins > 1 else ''}")

    msg.append(f"{secs} second{'s' if secs > 1 else ''}")

    return ' '.join(msg)
