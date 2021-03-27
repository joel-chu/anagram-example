/**
 * From v2 we split out the major methods and rename the method with
 * their version number, this way we can see how we progress with this application
 */

const { rearrangeLetters } = require('./lib/rearrange-letters')

/**
 * V.1
 * @BUG it will crash with a RangeError: Maximum call stack size exceeded
 * after 1000 calls, the reason is simple - too many calls to handle by the system
 * get a possible word that we haven't tried before
 * @param {string} str to scramble
 * @param {array} [triedsWords=[]] already tried word(s)
 * @return {string} a new scrambled word or false when there is none
 */
function getPossibleWordV1(str, triedWords = []) {
  const possibleWord = rearrangeLetters(str)
  const tried = triedWords.filter(w => w === possibleWord).length > 0
  if (tried) {

    return getPossibleWordV1(str, triedWords)
  }

  return possibleWord
}

/**
 * to get the stack finish before it continue, we could use the setTimeout trick
 * but once we employ this, the entire program structure will have to change
 *
 */
function getPossibleWordAsync(str, triedWords = [], _resovler = null) {

  const possibleWord = rearrangeLetters(str)

  const tried = triedWords.filter(w => w === possibleWord).length > 0
  // here we need to wrap the call in a promise
  return new Promise(resolver => {
    if (tried) {
      // this will effectively put the execution in the queue wait
      // and node will have time to release the stack
      setTimeout(() => {
        getPossibleWordAsync(str, triedWords, resolver)
      }, 0)
    } else {
      resolver(possibleWord)
    }
  })
}

// always export with this name
exports.getPossibleWord = getPossibleWordAsync
