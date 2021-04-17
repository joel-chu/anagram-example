# testing with pytest
# run it with `pytest code_test.py`

from mylib import getTotalCombinationNumFrp, getTotalCombinationNumRecursion
from db import getCharSeq

"""
num = 4

def test():
    assert getTotalCombinationNumFrp(num) == getTotalCombinationNumRecursion(num)
"""

def test1():
    assert getCharSeq("uoiea") == "aeiou"
