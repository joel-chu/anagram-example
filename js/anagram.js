// The main interface
const { join } = require('path')

const jsonData = require('../share/config.json')
const { MAX_CHAR, MIN_CHAR } = jsonData

const { getAnagram, getWords } = require('./lib')

const WORDS_DIR = join(__dirname, '..', 'share')

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
 * @public
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
  const result = Reflect.apply(anagram, null, args)

  if (result) {
    console.log(`We found the anagram for ${args[0]} > ${result}`)
  } else {
    console.error(`Sorry could not find anything`)
  }

} else {
  // using name export
  module.exports = { anagram }
}
