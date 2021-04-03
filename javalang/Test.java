import example.anagram.PubSub;

class Test {

  public static void main(String[] args) {

    int input = Integer.valueOf(args[0]);

    int total = getCombinationTotal(input, 0);

    // System.out.println(total);

    PubSub<Integer> ps = new PubSub<Integer>();

    ps.sub((value) -> {

      System.out.println("Getting value from the sub");
      System.out.println(value);

      return value;
    });

    ps.pub(total);

  }


  public static int getCombinationTotal(int n, int total) {
    if (n == 1) {
      return total;
    }
    if (total == 0) {
      total = n;
    }
    total = total * (n-1);
    --n;
    return getCombinationTotal(n, total);
  }

}
