package example.anagram;

// testing how to import the jar file
// import org.json.simple.JSONObject;
// import org.json.simple.JSONArray;
import org.json.simple.parser.ParseException;
import org.json.simple.parser.JSONParser;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class MyFileReader {
  // private String basePath;
  private Object nothingObj;
  private String nothingStr;

  // expect p to setup the basePath to the share folder

  public void MyFileReader(String p) {
    nothingObj = new Object();
    nothingStr = "";
  }

  /**
   * read a file into string, so much work for so little
   * @param pathToFile String where the file is
   * @return String the content of the file
   */
  public String getFileContent(String pathToFile) {
    try {
      // "../share/config.json"
      File jsonFileObj = new File(pathToFile);
      Scanner myReader = new Scanner(jsonFileObj);
      // note the <String> bit without it will fail with all kinds of error when compile
      ArrayList<String> list = new ArrayList<>();

      while (myReader.hasNextLine()) {
        String line = myReader.nextLine();
        list.add(line);
      }

      myReader.close();
      // join the list back as an String ...
      return String.join(" ", list);
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    // why the F javac expect a return statement here?
    return nothingStr;
  }

  // read the json file then return as json object
  public Object getJsonContent(String pathToJsonFile) {
    Object nothing = new Object();
    try {
      JSONParser parser = new JSONParser();
      String jsonString = getFileContent(pathToJsonFile);

      return parser.parse(jsonString);
    } catch(ParseException e) {
      System.out.println("Error position: " + e.getPosition());
      e.printStackTrace();
    }
    // why the F javac expect a return statement here
    return nothingObj;
  }

  // read the file then return it as an Array
  public String[] getWordsArray(String pathToFile) {
    String content = getFileContent(pathToFile);
    // what a piss off error - char using single quote ...
    // if I use single quote around the space, I get
    // error: incompatible types: char cannot be converted to String
    // System.out.println(content);

    return content.split(" ");
  }

}
