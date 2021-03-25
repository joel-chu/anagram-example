// define a package namespace
package example.anagram;

import java.util.*;
import example.anagram.*;
import org.json.simple.JSONObject;

public class MyLib {

  private String pathToWords;
  private JSONObject config;

  private MyFileReader reader;
  private ScrambleWords swObj;

  private String space = " ";

  // constructor
  public void MyLib(String pathToConfig, String ptw, String wordToTry) {
    // setup the required properties
    reader = new MyFileReader();
    config = reader.getJsonContent(pathToConfig);
    // setup for reuse
    pathToWords = ptw;
    swObj = new ScrambleWords(wordToTry);
  }

  // find the possible word of anagram in a recursion
  // the logic is
  // 1. generate a random word from the str
  // 2. check against the triedWords array if it's already tried
  // 3. If it's already tried (record outside) then try another one
  public String getPossibleWord(String str, ArrayList<String> triedWords) {
    // String possibleWord = scrambleWords(str);
    String possibleWord = swObj.getIt();
    if (triedWords.contains(possibleWord)) {

      return getPossibleWord(str, triedWords);
    }

    return possibleWord;
  }

  // import the words file return as array
  public String[] getWords(String dir, String name) {
    String fileExt = String.valueOf(this.config.get("FILE_EXT"));
    String dot = String.valueOf(this.config.get("DOT"));

    String[] filenameParts = { name, fileExt };

    String pathToFile = dir + String.join(dot, filenameParts);

    String fileContent = reader.getFileContent(pathToFile);

    return fileContent.split(space);
  }

  // there is no such thing as a filter ...
  public ArrayList<String> filteredWords(String str, String[] words) {
    // from https://stackoverflow.com/questions/10530353/convert-string-array-to-arraylist
    ArrayList<String> wordList = new ArrayList<>(Arrays.asList(words));
    int idx = wordList.indexOf(str);
    if (idx > -1) {
      wordList.remove(idx);
    }

    return wordList;
  }

  // the main method to get the anagram
  public String getAnagram(String str, String[] words) {
    ArrayList<String> dict = filteredWords(str, words);
    int len = dict.size();
    int maxTry = (int)Math.pow(2, len);
    int tried = 0;
    ArrayList<String> possibleWords = new ArrayList<>();

    while (tried <= maxTry) {
      String w = getPossibleWord(str, possibleWords);

      if (dict.contains(w)) {

        return w;
      }

      possibleWords.add(w);
      tried++;
    }

    // just return empty space, we just check the length
    return space;
  }
}
