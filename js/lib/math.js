// Calculation related methods

/**
 * Calculate possible combination total
 * @param {int} n the number of letters in the word
 * @param {int} total to hold the total number
 * @return {int} the total possible combination
 */
function getCombinationTotalRec(n, total = 0) {
    // exit cause
    if (n === 1) {
       return total
    }
    // init
    if (total === 0) {
       total = n
    }
    n--
    total *= n
    return getCombinationTotalRec(n, total)
}

/**
 * FRP version with nicer syntax
 * @param {int} n the last number
 */
function getCombinationTotalFrp(n) {
  // there is no range method in js yet
  // from: https://stackoverflow.com/questions/48892536/javascript-array-range
  const arr = Array.from({length: n + 1}, (_, i) => i)
  arr.shift()

  console.log(arr)

  return arr.reduce((a, b) => a * b, 1)
}

// expor the frp version
module.exports = {
    getCombinationTotal: getCombinationTotalFrp
}
