// Calculation related methods

/**
 * Calculate possible combination total
 * @param {int} n the number of letters in the word
 * @param {int} total to hold the total number
 * @return {int} the total possible combination
 */
function cpct(n, total = 0) {
    // exit cause
    if (n === 0) {
       return total
    }
    // init
    if (total === 0) {
       total = n
    }
    n--
    total += n
    return cpct(n, total)
}

function cpct_0(n, total = 0) {
    // exit cause
    if (n === 0) {
        return total
    }
    // init
    if (total === 0) {
        total = n
    }
    total = n + (n-1)
    n--
    return cpct(n, total)
}

const result1 = cpct_0(4)
const result2 = cpct_0(5)

console.log(result1, result2)
