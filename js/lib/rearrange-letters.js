/**
 * This was call scrambleWords when we just use the random
 * generator to scramble it, but later on we will try to
 * create combination based on it's possibility
 * therefore we rename it to rearrangeLetters instead
 */
const { fisherYates, shuffle } = require('./fisher-yates')


/**
 * scramble the characters
 * @param {string} str input
 * @return {string} scrambled character string
 */
exports.rearrangeLetters = function(str) {
  return shuffle(str.split('')).join('')
}
