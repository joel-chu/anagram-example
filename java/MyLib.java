// define a package namespace
package example.anagram;


public class MyLib {
  // declare a constructor
  public void MyLib() {

  }

  // randomized the array using Fisher Yates algorithm
  private String[] fisherYates(String[] arr) {
    int ctn = arr.length;

  }

  // scramble the word's character order
  private String scrambleWords(String str) {
    char[] charArray = str.toCharArray();
    char[] newCharArray = fisherYates(charArray);

    return String.join("", newCharArray);
  }

  // find the possible word of anagram
  private String getPossibleWord(String str, String[] triedWords) {

  }

  // imort the words file return as array
  public String[] getWords(String dir, String name) {


  }

  // the main method to get the anagram
  public String getAnagram(String str, String[] words) {

  }
}
