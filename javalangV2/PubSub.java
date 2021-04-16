
package example.anagram;

import example.anagram.*;
import java.util.*;
// can not use generic here

interface Command {
    public void run(String value);
}
// can we do PubSub<T> instead and pass it on to the Callback<T>?
public class PubSub {
  // when we try to init this Map store in the constructor
  // we got an nullPointerException which means it didn't created it
  private Map<String, Command> store = new HashMap<String, Command>();

  // we init the Command inside the sub call
  // instead we pass the Lambda as param
  public void sub(String name, Callback<String> cbInt) {
    store.put(name, new Command() {
      public void run(String value) {
        // this is wrong ...
        cbInt.cb(value);
      }
    });
  }

  public void pub(String name, String value) {
    store.get(name).run(value);
  }
}
