package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
public class ConvertBase {
  @EpiTest(testDataFile = "convert_base.tsv")

  public static String convertBase(String numAsString, int b1, int b2) {
    if (numAsString.equals("0") || numAsString.equals("-0")) return numAsString;
    boolean neg = false;
    int offset = 0;
    if (numAsString.charAt(0) == '-'){
      neg = true;
      offset = 1;
    }
    char[] charSeq = numAsString.toCharArray();
    int tot = 0;
    for (int i = offset; i < numAsString.length(); i ++){
      int curr = Character.isDigit(charSeq[i]) ? charSeq[i] - '0' : charSeq[i] - 'A' + 10;
      tot *= b1;
      tot += curr;
    }
    StringBuilder res = new StringBuilder();

    while (tot > 0){
      int newNum = tot % b2;
      char newNumAsChar = (char) (newNum < 10 ? '0' + newNum : 'A' + newNum - 10);

      tot = tot /b2;
      res.append(newNumAsChar);
    }

    return (neg ? "-" : "") + res.reverse().toString();
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "ConvertBase.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
