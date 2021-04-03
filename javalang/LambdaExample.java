
import example.anagram.Callback;

public class LambdaExample {

  public static void main(String[] args) {
    String str = args[0];
    int count = 0;
    // init the pubsub
    PubSub ps = new PubSub<String>();

    ps.sub((value) -> {
      System.out.println("Get result from PubSub callback");
      System.out.println(value);

      return "done"; // just to match the return type
    });
    // the actual Thread
    Thread t = new Thread(() -> someFuncToRun(str, count, ps));
    // start running the thread
    t.start();
  }

  public static String someFuncToRun(String str, int ctn, PubSub<String> ps) {
    ++ctn;
    if (ctn == 10) {
      return ps.pub("end here with result from callback");
    }
    System.out.println(ctn + " times");
    return someFuncToRun(str + " +1", ctn, ps);
  }
}

/* it just ridiculos 
class PubSub<T> {

  private Callback<T> cb;

  public void PubSub() {}

  public void sub(Callback<T> c) {
    cb = c;
  }

  public T pub(T value) {
    return cb.cb(value);
  }
}
*/
