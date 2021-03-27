// the library functions
const { getCombinationTotal } = require('./lib/math')
const { checkWord } = require('./lib/check-word')
const { getPossibleWord } = require('./get-possible-word')
/**
 * find the anagram from the input str
 * @param {string} str input word
 * @param {array} words list of words to search from
 * @return {*} success then we get the anagram or throw error
 * @public
 */
function getAnagramV1(str, words) {
  // we don't want the str in the list of words
  const dict = words.filter(s => s !== str)
  const len = str.length
  const maxTry = getCombinationTotal(len)
  let tried = 0
  let possibleWords = []
  while (tried <= maxTry) {
    // need to wrap this in a setTimeout( function() {}) but we need to rewrite this part
    const word = getPossibleWord(str, possibleWords)
    // is this word in the dictionary?
    if (dict.filter(w => w === word).length > 0) {
      // also return the tried number
      return [word, tried]
    }

    possibleWords.push(word)
    ++tried
  }

  return [false, tried]
}

/**
 * The async version of the getAnagram
 * Because the result is async therefore we can no longer use
 * the conventional while loop to check the result
 * instead we use another recursion to run this operation
 * Also to note is, we purposely not using async await here
 * we will in the next version
 * because we want to show you how you can solve the same problem in different ways
 * @param {string} str the input string to try
 * @param {array} dict the dictionary to compare against
 * @param {int} maxTry maximum number can try
 * @param {int} [tried=0] how many times we tried
 * @param {array} [possibleWord=[]] the word(s) we have tried so far
 * @param {function} resolver the Promise.resolver when we have an answer
 * @param {function} rejecter the Promise.rejecter when we don't have an answer
 * @return {promise} resolve / reject depends on the outcome
 */
function getAnagramAsync(str, dict, maxTry, tried = 0, possibleWord = [], resolver = null , rejecter = null) {
  return new Promise((_resolver, _rejecter) => {
    if (tried <= maxTry) {
      getPossibleWord(str, possibleWords)
        .then(word => {
          // is this word in the dictionary?
          if (dict.filter(w => w === word).length > 0) {
            // also return the tried number
            return resolver([word, tried])
          }
          possibleWords.push(word)
          ++tried
          setTimeout(() => {
            getAnagramAsync(str, dict, maxTry, tried, possibleWords, _resolver, _rejecter)
          }, 0)
        })
    } else {
      // if we could not find anything then we just reject it
      rejecter([false, tried])
    }
  })
}

/**
 * Here we prepare the necessary parameter for the getAnagramAsync
 *
 */
function getAnagram(str, words) {
  // here we also perform a check, since there are only so many word can have an anagram
  // we first check if this word can have one
  const inDict = checkWord(str, words)
  if (!inDict) {
    return Promise.reject([false, 0])
  }

  const dict = words.filter(s => s !== str)
  const len = str.length
  
  const maxTry = getCombinationTotal(len)

  return getAnagramAsync(str, dict, maxTry)
}

// now export the @public methods
module.exports = {
  getAnagram
}
