package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
public class IntSquareRoot {
  @EpiTest(testDataFile = "int_square_root.tsv")

  public static int squareRoot(int k) {
    if (k <= 1) return k;

    long l = 1, r = k;
    long guess = 1;
    while (l < r){

      guess = (l + r)/2;
      if (guess * guess <= k && Math.pow(guess+1,2) > k){
        return (int) guess;
      } else if (guess * guess > k){
        r = guess - 1;
      } else {
        l = guess + 1;
      }
    }
    return (int) l;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "IntSquareRoot.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
