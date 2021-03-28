// we put those methods that is not going to change
const path = require('path')
const fs = require('fs')

const { configJson } = require('./config-json')
const  { FILE_EXT, DOT, ENCODING } = configJson

/**
 * import the words file and turn into a usable format (array)
 * @param {string} dir the directory path
 * @param {*} name the name of the file
 * @return {array} of words
 * @public
 */
exports.getWords = function(dir, name) {
  const pathToFile = path.join(dir, [name + '', FILE_EXT].join(DOT))
  const content = fs.readFileSync(pathToFile, { encoding: ENCODING })

  return content.trim().split(' ')
}
