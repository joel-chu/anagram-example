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
const scrambleWords(str) => fisherYates(str.split('')).join('')

/**
 * import the words file and turn into a usable format (array)
 * @param {string} dir the directory path
 * @param {*} name the name of the file
 */
function getWords(dir, name) {
  const pathToFile = path.join(dir, name, DOT, FILE_EXT)
  const content = fs.readFileSync(pathToFile, {encoding: ENCODING})
  
}

function getAnagram(str, words) {

}
