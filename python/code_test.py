# testing with pytest
# run it with `pytest code_test.py`

from mylib import getTotalCombinationNumFrp, getTotalCombinationNumRecursion

num = 4

def test():
    assert getTotalCombinationNumFrp(num) == getTotalCombinationNumRecursion(num)
