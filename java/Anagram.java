import example.anagram.*;

final class Anagram {

  public static void main(String[] args) {
    String pathToConfig = "../share/config.json";
    String pathToWords = "../share/";

    runIt(args[0], pathToConfig, pathToWords);
  }

  // Wrap everything in one
  private static void runIt(String wordToTry, String pathToConfig) {
    int wordLen = wordToTry.length();

    MyLib anagramLib = new MyLib(pathToConfig, pathToWords, wordToTry);

    int maxChar = anagramLib.maxChar;
    int minChar = anagramLib.minChar;

    if (wordLen > maxChar || wordLen < minChar) {
      System.out.println("Error: please provide a word between " + minChar + " and " + maxChar);
    } else {
      String name = (String) wordLen;
      String[] words = anagramLib.getWords(pathToWords, name);
      String result = anagramLib.getAnagram(wordToTry, words);

      if (result.length > 1) {
          System.out.println("We found an angram for " + wordToTry + " > " + result);
      } else {
          System.out.println("Sorry could not find anything");
      }
    }
  }
}
