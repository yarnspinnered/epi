package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
public class Fibonacci {

  @EpiTest(testDataFile = "fibonacci.tsv")

  public static int fibonacci(int n) {
    if (n <= 1){
      return n;
    }
    int a = 0, b = 1, i = 2;

    while (i <= n){
      int tmp = b;
      b = a+b;
      a = tmp;
      i ++;
    }
    return b;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "Fibonacci.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
