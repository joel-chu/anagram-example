// we are spliting this part out on it's own
// and make it run on it's own thread
package example.anagram;

import java.util.*;
import example.anagram.*;

class GetPossibleWord {

  private final ScrambleWords swObj;
  private int maxTry;

  public GetPossibleWord(String initString, int mt) {
    swObj = new ScrambleWords(initString);
    maxTry = mt;
  }

  /**
   * find the possible word of anagram in a recursion
   * the logic is
   * 1. generate a random word from the str
   * 2. check against the triedWords array if it's already tried
   * 3. If it's already tried (record outside) then try another one
   */
  public String get(String str, ArrayList<String> triedWords, int i) {
    // String possibleWord = scrambleWords(str);
    String possibleWord = swObj.get();

    // System.out.println("Tried times: " + triedWords.size());
    ++i;

    if (triedWords.contains(possibleWord)) {

      return get(str, triedWords, i);
    }

    return possibleWord;
  }


}
