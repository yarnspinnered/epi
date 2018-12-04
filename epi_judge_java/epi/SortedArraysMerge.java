package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.*;

public class SortedArraysMerge {
  private static class Pair{
    int val;
    Iterator<Integer> iter;

    public Pair(int val, Iterator<Integer>  iter){
      this.val = val;
      this.iter = iter;
    }


  }
  @EpiTest(testDataFile = "sorted_arrays_merge.tsv")

  public static List<Integer>
  mergeSortedArrays(List<List<Integer>> sortedArrays) {
    PriorityQueue<Pair> heap = new PriorityQueue<Pair>(sortedArrays.size(), (Pair a, Pair b)-> Integer.compare(a.val,b.val));
    for (List<Integer> l : sortedArrays){
      if (!l.isEmpty()){
        Iterator<Integer> it = l.iterator();
        Integer v = it.next();
        heap.add(new Pair(v,it));
      }
    }
    List<Integer> res = new ArrayList<>();
    while (!heap.isEmpty()){
      Pair current = heap.poll();
      if (current.iter.hasNext()) {
        heap.add(new Pair(current.iter.next(), current.iter));
      }
      res.add(current.val);
    }
    return res;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "SortedArraysMerge.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
