// we are spliting this part out on it's own
// and make it run on it's own thread
package examle.anagram;
import java.util.*;
import example.anagram.*;

class GetPossibleWord {

  private final ScrambleWords swObj;

  public GetPossibleWord(ScrambleWords obj) {
    swObj = obj;
  }

  /**
   * find the possible word of anagram in a recursion
   * the logic is
   * 1. generate a random word from the str
   * 2. check against the triedWords array if it's already tried
   * 3. If it's already tried (record outside) then try another one
   */
  public String getPossibleWordAction(String str, ArrayList<String> triedWords, int maxTryAllow, int i) {
    // String possibleWord = scrambleWords(str);
    String possibleWord = swObj.getIt();

    System.out.println("Tried times: " + triedWords.size());

    if (triedWords.contains(possibleWord)) {

      return getPossibleWordAction(str, triedWords);
    }

    return possibleWord;
  }


}
