// define a package namespace
package example.anagram;

import java.util.*;
import example.anagram.*;
import org.json.simple.JSONObject;

public class MyLib {

  private JSONObject configObj;
  private MyFileReader reader;

  private String[] dictWords;

  private String space = " ";
  // @NOTE: JSONObject doesn't return int ...
  public long maxChar;
  public long minChar;

  // constructor
  public MyLib(String pathToConfig, String wordToTry) {
    // setup the required properties
    reader = new MyFileReader();
    configObj = reader.getJsonContent(pathToConfig);
    // prepare for use later
    maxChar = (long) configObj.get("MAX_CHAR");
    minChar = (long) configObj.get("MIN_CHAR");

  }

  // import the words file return as array
  public String[] getWords(String dir, String name) {
    String fileExt = String.valueOf(configObj.get("FILE_EXT"));
    String dot = String.valueOf(configObj.get("DOT"));

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
      System.out.println("tried: " + tried);

      GetPossibleWord wordGetter = new GetPossibleWord(str);
      String w = wordGetter.get(str, possibleWords);

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
