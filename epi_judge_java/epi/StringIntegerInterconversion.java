package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
import epi.test_framework.TestFailure;

public class StringIntegerInterconversion {

  public static String intToString(int x) {
    if (x == 0){
      return "0";
    }
    StringBuilder res = new StringBuilder();
    boolean neg = false;
    if (x < 0){
      neg = true;
    }
    while (x != 0){
      char offset = (char) Math.abs((x % 10));
      offset += '0';
      x /= 10;

      res.append(offset);
    }

    if (neg){
      res.append('-');
    }

    String result = res.reverse().toString();
    return result;
  }
  public static int stringToInt(String s) {
    int res = 0;
    boolean negative = false;

    if (s.charAt(0) == '-'){
      negative = true;
      s = s.substring(1,s.length());
    }
    for (int i = 0; i < s.length(); i ++){
      res *= 10;
      res += s.charAt(i) - '0';
    }

    return negative ? -res : res;
  }
  @EpiTest(testDataFile = "string_integer_interconversion.tsv")
  public static void wrapper(int x, String s) throws TestFailure {
    if (!intToString(x).equals(s)) {
      throw new TestFailure("Int to string conversion failed");
    }
    if (stringToInt(s) != x) {
      throw new TestFailure("String to int conversion failed");
    }
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "StringIntegerInterconversion.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
