package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.EpiTestComparator;
import epi.test_framework.LexicographicalListComparator;
import epi.test_framework.GenericTest;

import java.util.*;
import java.util.function.BiPredicate;
public class Anagrams {
  @EpiTest(testDataFile = "anagrams.tsv")

  public static List<List<String>> findAnagrams(List<String> dictionary) {
    HashMap<String, List<String>> stringDict = new HashMap<>();
    for (String s: dictionary){
      char[] charSeq = s.toCharArray();
      Arrays.sort(charSeq);
      String canonicalForm = new String(charSeq);
      if (stringDict.containsKey(canonicalForm)){
        stringDict.get(canonicalForm).add(s);
      } else {
        List<String> newList = new LinkedList<>();
        newList.add(s);
        stringDict.put(canonicalForm, newList);
      }
    }

    List<List<String>> res = new ArrayList<>(stringDict.values());
    res.removeIf((List<String> l ) -> l.size() < 2 );
    return res;
  }
  @EpiTestComparator
  public static BiPredicate<List<List<String>>, List<List<String>>> comp =
      (expected, result) -> {
    if (result == null) {
      return false;
    }
    for (List<String> l : expected) {
      Collections.sort(l);
    }
    expected.sort(new LexicographicalListComparator<>());
    for (List<String> l : result) {
      Collections.sort(l);
    }
    result.sort(new LexicographicalListComparator<>());
    return expected.equals(result);
  };

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "Anagrams.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
