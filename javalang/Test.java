
public class Test {

  public static void main(String[] args) {
    String str = args[0];
    int count = 0;
    Thread t = new Thread(() -> someFuncToRun(str, count));
    t.start();
  }

  public static String someFuncToRun(String str, int ctn) {
    ++ctn;
    if (ctn == 10) {
      return "end";
    }
    System.out.println(ctn + " times");
    return str + " world";
  }
}
