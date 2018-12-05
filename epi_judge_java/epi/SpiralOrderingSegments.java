package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
public class SpiralOrderingSegments {
  @EpiTest(testDataFile = "spiral_ordering_segments.tsv")

  public static List<Integer>
  matrixInSpiralOrder(List<List<Integer>> squareMatrix) {
    if (squareMatrix.size() == 0){
      return List.of();
    }
    List<List<Integer>> directions = List.of(List.of(0,1), List.of(1,0), List.of(0,-1), List.of(-1,0));
    int directionsPos = 0;
    int total = squareMatrix.size() * squareMatrix.size();
    int i = 0;
    int j = 0;
    HashSet<List<Integer>> seen = new HashSet<>();
    int it = 0;
    List<Integer> res = new ArrayList<>();
    while (it < total){
      res.add(squareMatrix.get(i).get(j));
      seen.add(List.of(i,j));
      int continue_i = i + directions.get(directionsPos).get(0);
      int continue_j = j + directions.get(directionsPos).get(1);
      if (0 <= continue_i
          && continue_i < squareMatrix.size()
          && 0 <= continue_j
          && continue_j < squareMatrix.size()
          && !seen.contains(List.of(continue_i, continue_j))){

        i = continue_i;
        j = continue_j;
      } else {
        directionsPos = (directionsPos + 1) % 4;
        i += directions.get(directionsPos).get(0);
        j += directions.get(directionsPos).get(1);
      }
      it++;

    }
    return res;
  }

  public static void main(String[] args) {
    System.out.println(matrixInSpiralOrder(List.of(List.of(1,2), List.of(3,4))));
    System.exit(
        GenericTest
            .runFromAnnotations(args, "SpiralOrderingSegments.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
