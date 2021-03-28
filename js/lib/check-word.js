
/**
 * Because there are only so many words can have an anagram
 * we could first check the word provide is in the dictionary
 * @param {string} word the word user provide
 * @param {array} dict the dictionary
 * @return {boolean} return false if that word is not in the dict
 */
exports.checkWord = function(word, dict) {
  // we don't use the indexOf because it could be wrong
  return dict.filter(w => w === word).length > 0
}
