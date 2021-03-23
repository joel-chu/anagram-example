// The main interface
const { join } = require('path')

const { MAX_CHAR, MIN_CHAR } = require('./constants')
const { getAnagram, getWords } = require('./lib')

const WORDS_DIR = join(__dirname, '..', 'words')

/**
 * The main interface to run the anagram program
 * It takes in the word and import the appropriate dictionary
 * then call the actual program
 *
 * Note here we only accept one word at a time here
 * if you want to pass sentence, then wrap this call in a map fn
 *
 * @param {string} str the input string
 * @return {string} the anagram or throw if there is an error
 */
function anagram(str) {
  const len = str.length;
  if (len > MAX_CHAR || len < MIN_CHAR) {
    throw new Error(`Error: please provide a word between ${MIN_CHAR} and ${MAX_CHAR} `)
  }
  const words = getWords(WORDS_DIR, len)

  return getAnagram(str, words)
}

// finally check if it's call from cmd or not
if (require.main === module) {
  const args = process.argv.slice(2)
  // could do a bit more wording hint etc, but that will be some other time
  Reflect.call(null, anagram, args)

} else {
  // using name export
  module.exports = { anagram }
}
