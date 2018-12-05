package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.*;

public class TreeLevelOrder {
  private static class NodeInfo<T> {
    BinaryTreeNode<T> node;
    int depth;

    public NodeInfo(BinaryTreeNode<T> node, int depth){
      this.node = node;
      this.depth = depth;
    }
  }
  @EpiTest(testDataFile = "tree_level_order.tsv")

  public static List<List<Integer>>
  binaryTreeDepthOrder(BinaryTreeNode<Integer> tree) {
    if (tree == null){
      return new ArrayList<>();
    }

    Deque<NodeInfo> queue = new ArrayDeque<>();
    queue.add(new NodeInfo<Integer>(tree, 0));
    List<List<Integer>> res = new ArrayList<>();

    while (!queue.isEmpty()){
      NodeInfo currInfo = queue.poll();
      BinaryTreeNode<Integer> u = currInfo.node;
      int depth = currInfo.depth;

      if (u.left != null){
        queue.add(new NodeInfo<Integer>(u.left, depth + 1));
      }
      if (u.right != null){
        queue.add(new NodeInfo<Integer>(u.right, depth + 1));
      }

      if (res.size() > depth){
        List<Integer> listToUpdate = res.get(depth);

        listToUpdate.add(u.data);
      } else {
        ArrayList<Integer> newList = new ArrayList<Integer>();
        newList.add(u.data);
        res.add(newList);
      }
    }
    return res;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "TreeLevelOrder.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
