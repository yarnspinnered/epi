package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class IntersectSortedArrays {
  @EpiTest(testDataFile = "intersect_sorted_arrays.tsv")

  public static List<Integer> intersectTwoSortedArrays(List<Integer> A,
                                                       List<Integer> B) {
    int l = 0, r = 0;
    ArrayList<Integer> res = new ArrayList<>();
    while (l < A.size() && r < B.size()){
      if (A.get(l) < B.get(r)){
        l += 1;
      } else if (A.get(l) > B.get(r)){
        r += 1;
      } else {
        if (res.isEmpty() || A.get(l) > res.get(res.size() - 1)){
          res.add(A.get(l));
        }
        l += 1;
      }
    }
    return res;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "IntersectSortedArrays.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
