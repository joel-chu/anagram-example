// breaking out the scramble word method
// it just way too much work to produce so little
package example.anagram;

import java.util.*;

public class ScrambleWords {

  // scramble the word's character order
  public String ScrambleWords(String str) {

    // need to turn the char[] into String[] before we can use
    String[] usableStrArr = stringToStringArray(str);
    String[] newCharArray = fisherYates(usableStrArr);

    return String.join("", newCharArray);
  }


  // randomized the array using Fisher Yates algorithm
  private String[] fisherYates(String[] arr) {
    int ctn = arr.length;
    for (int i = ctn - 1; i > 0; i--) {
      Random r = new Random();
      // Java round return int floor return double
      int j = Math.round(r * (i + 1));
      String temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
    return arr;
  }

  // another converting one type (ArrayList) to anther (String[])
  private String[] getStringArray(ArrayList<String> arr) {
    int ctn = arr.size();
    // declaration and initialise String Array
    String str[] = new String[ctn];
    // ArrayList to Array Conversion
    for (int i = 0; i < ctn; i++) {
      // Assign each value to String array
      str[i] = arr.get(i);
    }
    return str;
  }

  // another PIA when you try to convert char to string
  // char is primitive type String is an object, therefore
  // char can not get dereference and transform into another type
  private String[] stringToStringArray(String word) {
    char[] f = word.toCharArray();
    int c = f.length;

    ArrayList<String> data = new ArrayList<>();
    for (int i = 0; i < c; i++) {
      data.add(String.valueOf(f[i]));
    }
    return getStringArray(data);
  }

}
