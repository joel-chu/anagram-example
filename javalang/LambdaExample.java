
import example.anagram.Callback;

public class LambdaExample {

  public static void main(String[] args) {
    String str = args[0];
    int count = 0;

    Thread t = new Thread(() ->
      someFuncToRun(str, count, (value) -> {
        System.out.println(value);
        return value;
      }));

    t.start();
  }

  public static String someFuncToRun(String str, int ctn, Callback<String> cb) {
    ++ctn;
    if (ctn == 10) {
      System.out.println("End here");
      return cb.cb("end");
    }
    System.out.println(ctn + " times");
    return someFuncToRun(str + " +1", ctn, cb);
  }
}
