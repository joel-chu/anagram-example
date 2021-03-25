// define a package namespace
package example.anagram;

import java.util.*;
import example.anagram.MyFileReader;

public class MyLib {

  private MyFileReader reader;
  private Object config;

  // declare a constructor
  public void MyLib(String pathToConfig) {
    // setup the required properties
    reader = new MyFileReader();
    config = reader.getJsonContent(pathToConfig);
  }



  // wrap the check in online because it's
  // not as simple as in JS
  private Boolean hasTried(String word, String[] triedWords) {

  }

  // find the possible word of anagram
  private String getPossibleWord(String str, String[] triedWords) {
    String possibleWord = scrambleWords(str);

  }

  // imort the words file return as array
  public String[] getWords(String dir, String name) {


  }

  // the main method to get the anagram
  public String getAnagram(String str, String[] words) {

  }
}
