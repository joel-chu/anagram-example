// the library functions
const path = require('path')
const fs = require('fs')

const { FILE_EXT, DOT, ENCODING } = require('./constants')

/**
 * Randomly rearrange an array using Fisher Yates algorithm
 * @param {array} arr input array
 * @return {array} randomized array
 */
function fisherYates(arr) {
  const ctn = arr.length
  for (let i = ctn - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    const temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
  }

  return arr
}

/**
 * scramble the characters
 * @param {string} str input
 * @return {string} scrambled character string
 */
const scrambleWords = (str) => fisherYates(str.split('')).join('')

/**
 * get a possible word that we haven't tried before
 * @param {string} str to scramble
 * @param {array} [triedsWords=[]] already tried word(s)
 * @return {string} a new scrambled word or false when there is none
 */
function getPossibleWord(str, triedWords = []) {
  const possibleWord = scrambleWords(str)
  const tried = triedWords.filter(w => w === possibleWord).length > 0
  if (tried) {

    return getPossibleWord(str, triedWords)
  }

  return possibleWord
}

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
  const dictLen = words.length

  const len = str.length
  const maxTried = Math.pow(2, len)

  let tried = 0
  let possibleWords = []

  while (tried <= maxTried) {
    const word = getPossibleWord(str, possibleWords)

    // is this word in the dictionary?
    if (dict.filter(w => w === word).length > 0) {
      return word
    }

    possibleWords.push(word)
    ++tried
  }

  return false
}


// now export the @public methods
module.exports = {
  getWords,
  getAnagram
}
