
package example.anagram;

import java.util.*;
// can not use generic here
interface Command {
    public void runCommand(String value);
}

/**
To use this stupid piece of crap
You need to do it like this

ps.sub(name, new Command() {
  public void runCommand(String value) {
    // this is where you put your code
  };
});

**/

class PubSub {

  private Map<String,Command> store = new HashMap<String, Command>();

  public void sub(String name, Command c) {
    store.put(name, c);
  }

  public void pub(String name, String value) {
    store.get(name).runCommand(value);
  }
}
