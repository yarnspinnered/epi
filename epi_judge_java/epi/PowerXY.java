package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
public class PowerXY {
  @EpiTest(testDataFile = "power_x_y.tsv")
  public static double power(double x, int y) {
    if (y == 1){
      return x;
    } else if (y == 0){
      return 1;

    } else if (y < 0) {
      return 1 / power(x,-y);
    }

    if (y % 2 == 0){
      return power(x*x, y/2);
    } else {
      return x * power(x, y - 1);
    }
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "PowerXY.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
