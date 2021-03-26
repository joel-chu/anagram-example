// the library functions
const path = require('path')
const fs = require('fs')

const jsonData = require('../share/config.json')
const { FILE_EXT, DOT, ENCODING } = jsonData

const { getCombinationTotal } = require('./math')
const { getPossibleWord } = require('./get-possible-word')

/**
 * import the words file and turn into a usable format (array)
 * @param {string} dir the directory path
 * @param {*} name the name of the file
 * @return {array} of words
 * @public
 */
function getWords(dir, name) {
  const pathToFile = path.join(dir, [name + '', FILE_EXT].join(DOT))
  const content = fs.readFileSync(pathToFile, { encoding: ENCODING })

  return content.trim().split(' ')
}

/**
 * find the anagram from the input str
 * @param {string} str input word
 * @param {array} words list of words to search from
 * @return {*} success then we get the anagram or throw error
 * @public
 */
function getAnagram(str, words) {
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


// now export the @public methods
module.exports = {
  getWords,
  getAnagram
}
