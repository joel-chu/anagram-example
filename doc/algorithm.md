# Algorithm 

Anagram is a game as old as the language itself. There are already plenty of other implementation.
But it's always good to first **think** about how to do it, before you look at how the other people did it.
And algorithm is at the heart of this game. So here I explain a bit what did I use, and why. 

## Reference  

The calculations and algorithm are coming from the following websites:

- [math.stackexchange.com](https://math.stackexchange.com/questions/876352/how-can-i-calculate-the-total-number-of-possible-anagrams-for-a-set-of-letters) 
- [wikipedia](https://en.wikipedia.org/wiki/Rule_of_product)
- [wikihow.com](https://www.wikihow.com/Calculate-Combinations)
- [Free Online Calculator](https://www.free-online-calculator-use.com/combination-calculator.html) (For checking the result)

## The basic idea 

Basically, you get a word (English), then scramble the characters, then hopefully you find 
another correct (English) word. 

First, you might try to list out everything possible combination. Let's try 3 letters.

```
cat
cta
act
atc
tca
tac
```

So a 3 letters long word can have 6 different combinations. What about 4 letters.

```
aces
caes
eacs
aecs
ceas
ecas
scae
csae
asce
sace
case
acse
aesc
easc
saec
asec
esac
seac
seca
esca
csea
scea
ecsa
cesa
```

A 4 letters long word can have up to 24 different combinations. One extra letter create quite a big jump in numbers of possibilities. 

The formula to calculation all possible combination is like this 

```
3 * 2 = 6
4 * 3 * 2 = 24
5 * 4 * 3 * 2 = 120
``` 

For proper mathematics equation representation can see the reference section above. 

Now we need to use computer language to calculate the result. Here I am using Javascript.

```js 
// version 1
// calculate possible combination total 
function getCombinationTotal(n, total = 0) {
    // exit cause
    if (n === 1) {
       return total
    }
    // init
    if (total === 0) {
       total = n
    }
    n--
    total *= n
    return getCombinationTotal(n, total)
}
```
Now here is another problem, what if we put a 15 letters long word, 
how many combination would that be?

**1,307,674,368,000**

Thats over a trillion possibilities ...

In the version 1 of this program, I only use a random generator to half solve this problem, 
basically it's like rolling a dice, and see if I bet on the right one. 

To be continue ... 
