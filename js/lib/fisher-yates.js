/**
 * If we only have one method to export 
 * then we don't need the full module.exports
 */

/**
 * Randomly rearrange an array using Fisher Yates algorithm
 * @param {array} arr input array
 * @return {array} randomized array
 */
exports.fisherYates = function(arr) {
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
 * in javascript we could do the same thing so much easier
 * @param {array} arr input array
 * @return {array} randomized array
 */
exports.shuffle = arr => arr.slice().sort(() => Math.random() - 0.5)