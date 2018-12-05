package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
import java.util.List;
public class TwoSortedArraysMerge {

  public static void mergeTwoSortedArrays(List<Integer> A, int m,
                                          List<Integer> B, int n) {
    int toFill = m + n - 1;
    int i = m - 1, j = n - 1;
    while (i >= 0 && j >= 0){
      int a = A.get(i);
      int b = B.get(j);
      if (a > b){
        A.set(toFill, a);
        i--;
      } else {
        A.set(toFill, b);
        j--;
      }
      toFill--;
    }

    while (j >= 0){
      A.set(toFill--, B.get(j--));
    }
    return;
  }
  @EpiTest(testDataFile = "two_sorted_arrays_merge.tsv")
  public static List<Integer>
  mergeTwoSortedArraysWrapper(List<Integer> A, int m, List<Integer> B, int n) {
    mergeTwoSortedArrays(A, m, B, n);
    return A;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "TwoSortedArraysMerge.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
