package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.EpiUserType;
import epi.test_framework.GenericTest;
import epi.test_framework.TestFailure;

import java.util.*;

public class SearchMaze {
  @EpiUserType(ctorParams = {int.class, int.class})

  public static class Coordinate {
    public int x, y;

    public Coordinate(int x, int y) {
      this.x = x;
      this.y = y;
    }

    @Override
    public boolean equals(Object o) {
      if (this == o) {
        return true;
      }

      if (o == null || getClass() != o.getClass()) {
        return false;
      }

      Coordinate that = (Coordinate)o;
      if (x != that.x || y != that.y) {
        return false;
      }
      return true;
    }
    @Override
    public int hashCode(){
      return Objects.hash(this.x, this.y);
    }
    @Override
    public String toString(){
      return this.x + " " + this.y;
    }
  }

  public enum Color { WHITE, BLACK }

  public static boolean dfs(List<List<Color>> maze, HashMap<Coordinate, Coordinate> parent, Coordinate currPos, Coordinate destPos){
    if (currPos.equals(destPos)){
      return true;
    }
    List<List<Integer>> directions = List.of(List.of(0,1), List.of(0,-1), List.of(1,0), List.of(-1,0));
    int x = currPos.x;
    int y = currPos.y;
    for (List<Integer> d : directions){
      int new_x = x + d.get(0);
      int new_y = y + d.get(1);
      Coordinate newPos = new Coordinate(new_x, new_y);
      if (0 <= new_x && new_x < maze.size() && 0 <= new_y &&
              new_y < maze.get(new_x).size()
              && maze.get(new_x).get(new_y) == Color.WHITE
              && !parent.containsKey(newPos)){
        parent.put(newPos, currPos);
        boolean success = dfs(maze, parent, newPos, destPos);
        if (success){
//          parent.put(newPos, currPos);
          return true;
        }
      }
    }
    return false;
  }
  public static List<Coordinate> searchMaze(List<List<Color>> maze,
                                            Coordinate s, Coordinate e) {
    HashMap<Coordinate, Coordinate> parent = new HashMap<>();
    parent.put(s, null);
    dfs(maze, parent, s, e);

    Coordinate curr = e;
    Deque<Coordinate> deque = new LinkedList<>();
    if (parent.containsKey(e)){
      while (e != null){
        deque.addFirst(e);
        e = parent.get(e);

      }
    }

    return new ArrayList<Coordinate>(deque);
  }
  public static boolean pathElementIsFeasible(List<List<Integer>> maze,
                                              Coordinate prev, Coordinate cur) {
    if (!(0 <= cur.x && cur.x < maze.size() && 0 <= cur.y &&
          cur.y < maze.get(cur.x).size() && maze.get(cur.x).get(cur.y) == 0)) {
      return false;
    }
    return cur.x == prev.x + 1 && cur.y == prev.y ||
        cur.x == prev.x - 1 && cur.y == prev.y ||
        cur.x == prev.x && cur.y == prev.y + 1 ||
        cur.x == prev.x && cur.y == prev.y - 1;
  }

  @EpiTest(testDataFile = "search_maze.tsv")
  public static boolean searchMazeWrapper(List<List<Integer>> maze,
                                          Coordinate s, Coordinate e)
      throws TestFailure {
    List<List<Color>> colored = new ArrayList<>();
    for (List<Integer> col : maze) {
      List<Color> tmp = new ArrayList<>();
      for (Integer i : col) {
        tmp.add(i == 0 ? Color.WHITE : Color.BLACK);
      }
      colored.add(tmp);
    }
    List<Coordinate> path = searchMaze(colored, s, e);
    if (path.isEmpty()) {
      return s.equals(e);
    }

    if (!path.get(0).equals(s) || !path.get(path.size() - 1).equals(e)) {
      throw new TestFailure("Path doesn't lay between start and end points");
    }

    for (int i = 1; i < path.size(); i++) {
      if (!pathElementIsFeasible(maze, path.get(i - 1), path.get(i))) {
        throw new TestFailure("Path contains invalid segments");
      }
    }

    return true;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "SearchMaze.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
