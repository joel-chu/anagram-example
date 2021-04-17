# math related methods put here
def getTotalCombinationNumRecursion(n, total = 0):
    """
    The old calculation was wrong, we need the total possible combination number
    which is Xn ... X2 * X1 = total
    This example to actually show you the math inside
    """
    if (n == 1):
        return total
    if (total == 0):
        total = n
    n -= 1
    total *= n
    return getTotalCombinationNumRecursion(n, total)

def getTotalCombinationNumFrp(n):
    """
    Same result as above but using a FRP style
    Although we get the same result but this one it's harder to know the math
    """

    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

def getTotalCombinationNum(n):
    """
    wrapper method
    """
    return getTotalCombinationNumFrp(n)