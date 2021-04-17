# generate word related methods put here
import random
import math

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

def shuffleArray(arr):
    """
    A more frp style approach to solve the same problem
    """


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