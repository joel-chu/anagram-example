# RecursionError: maximum recursion depth exceeded in comparison

If you have tried to run the Python version of the anagram program with 5 letters word.
You should have seen the above error raised.

What happened was the recursive function call have exceed the system allow.

If you want to know how many times your system allow you to run one function recursively.
You can try the following

```python
import sys
print(sys.getrecursionlimit())
```

On my system show `1000`. But a 5 letters word might need to run over 5000 times in recursion
to find the possible answer. Some on the internet suggest to raise that limit:

```python
import sys
sys.setrecursionlimit(5000)
```

But that's unsafe, you don't really want to mess with the Python setting.
Also what if we don't know how many times we need to run that loop before we get an answer?

Another suggestion (the number 1 search result on Bing) said you should use **Iterative Algorithm**.
Which in effect, run a big long loop, I personally think that is just _moronic_, and a rewrite
like what it suggested could introduce problem to the other part of your program. Further more,
that doesn't help to solve the problem we face, because we don't know how many loops we need
to get an answer.

What we want to do is to fix that function **ONLY**.

## One possible solution - divide and conquer

Here I am going to try a different approach (The node.js version also face a similar problem,
and it was fixed by using what the language allow you to do. And [you can read about it here.](./changelog.md))

There is another way to deal with this problem. By not allow each recursive call exceed that amount that is allow.

Let's take a look at the following example:

```python
def run(i, m):
    if (i == m):
        return i
    else:
        i += 1
        return run(i, m)
```

If we set the argument `m` value to be more than the above mentioned `sys.getrecursionlimit()`,
then we will surely see the error. If we set it to under it, then it works without problem.
Therefore, all we have to do is divide the whole task by the number that is allow, and run it
one after another.

```python
import sys
import math

maxAllow = math.floor(sys.getrecursionlimit()*0.9)
max = 5000 # we want to run 5000 times

units = math.ceil(max / maxAllow)

def run(i, m):
    if (i == m):
        return i
    else:
        i += 1
        return run(i, m)

def runWrapper(u):
    i = 0
    j = 1
    while (u):
        print(f"Unit {u} is running, i = {i}")
        ma = j * maxAllow
        if (ma >= max):
            ma = max
        print(f"ma = {ma}")
        i = run(i, ma)
        u -= 1
        j += 1
    return i

result = runWrapper(units)
print(f"result = {result}")
```

Now your recursive function will run 5000 times in 6 separate calls without any error.
The advantage of this approach is, you don't need to completely rewrite your recursive function,
just need to introduce new parameter, and a outer wrapper method to break it down.
And the refactor will introduce minimum disruption to your entire program.

## The fix to our code

It turns out it's easier than we think. We just need to introduce the `recursionLimit` and `i`
parameter to the function:

```python
import sys
# Get the number of maximum recursion calls
# we only use 90% of what its allow on the safe side
# in fact the number is not accurate, system report 1000 but the
# recursion stop at 997
recursionLimit = sys.getrecursionlimit() * 0.9

def getPossibleWord(str, triedWords, recursionLimit, i = 0):
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
        return getPossibleWord(str, triedWords, recursionLimit, i)

    return possibleWord    
```

What happen is, in the function that call the  `getPossibleWord`. We just need it to
be aware when the result return a `False` that means the recursion has reach it's limit.
And skip one count, and call it again. Therefore, it create the same effects like what we describe above.
