#!/usr/bin/env node

const readline = require('readline')
// this will be the interative version
// we just import the anagram method
const { runAnagramProgram } = require('./anagram')

// wrap this in one call
function main() {

  console.log(`Type 'quit()' or CTRL-C to exit this program`)

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  })

  rl.question("Please give me a word: ", (value) => {
    if (value === "quit()") {
      rl.close()
      // process.exit(0)
    } else {
      runAnagramProgram(value)
        .then(() => {
          rl.close()
        })
    }
  })
}

// now run it
main()
