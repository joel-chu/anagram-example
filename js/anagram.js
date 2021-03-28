// The main interface
const { join } = require('path')

const { getWords } = require('./lib/get-words')
const { getAnagram } = require('./get-anagram')

const { configJson } = require('./lib/config-json')
const { MAX_CHAR, MIN_CHAR } = configJson

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
    return console.error(`Error: please provide a word between ${MIN_CHAR} and ${MAX_CHAR} `)
  }
  const words = getWords(WORDS_DIR, len)

  return getAnagram(str, words)
}

// finally check if it's call from cmd or not
if (require.main === module) {
  const args = process.argv.slice(2)

  if (!args.length) {
    return console.error(`You need to provide a word`)
  }

  // V.2 we change this to a Promise interface
  Reflect.apply(anagram, null, args)
    .then(result => {
      const [ word, tried ] = result;
      console.log(`We found the anagram for ${args[0]} > ${word}, after we guess ${tried} time${tried > 1 ? 's' : ''}`)
    })
    .catch(error => {
      console.log(typeof error, error)

      const [, tried] = error
      console.error(`Sorry could not find anything, after try ${tried} times.`)
    })
} else {
  // name export it again
  module.exports = { anagram }
}
