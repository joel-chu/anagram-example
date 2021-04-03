
package example.anagram;

import example.anagram.Callback;

class PubSub<T> {

  private Callback<T> cb;

  public void sub(Callback<T> c) {
    cb = c;
  }

  public T pub(T value) {
    return cb.cb(value);
  }
}
