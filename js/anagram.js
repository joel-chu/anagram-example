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
  const len = str.length
  if (len > MAX_CHAR || len < MIN_CHAR) {
    return Promise.reject([null, `Error: please provide a word between ${MIN_CHAR} and ${MAX_CHAR}`])
  }
  const words = getWords(WORDS_DIR, len)

  return getAnagram(str, words)
}

// wrap everything together
function runAnagramProgram(arg) {
  // V.2 we change this to a Promise interface
  return anagram(arg)
    .then(result => {
      const [ word, tried ] = result
      console.log(`We found the anagram for ${arg} > ${word}, after we guess ${tried} time${tried > 1 ? 's' : ''}`)
    })
    .catch(error => {
      try {
        // @TODO if there is an real error instead of the value we return
        // this will not work correctly
        const [result, tried] = error
        if (result === false) {
          console.error(`Sorry could not find anything, after try ${tried} times.`)
        } else {
          console.error(tried)
        }
      } catch(e) {
        console.error(`An error occuried`, error)
      }
    })
}

// finally check if it's call from cmd or not
if (require.main === module) {
  const args = process.argv.slice(2)

  if (!args.length) {
    return console.error(`You need to provide a word`)
  }

  Reflect.apply(runAnagramProgram, null, args)

} else {
  // name export it again
  module.exports = { anagram, runAnagramProgram }
}
