package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
import java.util.List;
public class SearchFirstKey {
  @EpiTest(testDataFile = "search_first_key.tsv")

  public static int searchFirstOfK(List<Integer> A, int k) {
    int l,r, candidate;
    l = 0;
    r = A.size() - 1;
    candidate = -1;

    while (l <= r){
      int m = (l +r)/2;
      if (A.get(m) == k){
        candidate = m;
        r = m - 1;
      } else if (A.get(m) < k){
        l = m + 1;
      } else {
        r = m - 1;
      }
    }
    return candidate;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "SearchFirstKey.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
