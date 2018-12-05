package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.HashMap;
import java.util.List;
public class NearestRepeatedEntries {
  @EpiTest(testDataFile = "nearest_repeated_entries.tsv")

  public static int findNearestRepetition(List<String> paragraph) {
    HashMap<String, Integer> mostRecent = new HashMap<>();
    int best = Integer.MAX_VALUE;
    int pos = 0;
    for (String w : paragraph){
      if (mostRecent.containsKey(w)){
        int prevPos = mostRecent.get(w);
        best = Math.min(best, pos-prevPos);
      }
      mostRecent.put(w, pos);

      pos++;
    }
    return best == Integer.MAX_VALUE ? -1 : best;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "NearestRepeatedEntries.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
