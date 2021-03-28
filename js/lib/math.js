// Calculation related methods

/**
 * Calculate possible combination total
 * @param {int} n the number of letters in the word
 * @param {int} total to hold the total number
 * @return {int} the total possible combination
 */
function getCombinationTotal(n, total = 0) {
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
    return getCombinationTotal(n, total)
}

module.exports = {
    getCombinationTotal
}