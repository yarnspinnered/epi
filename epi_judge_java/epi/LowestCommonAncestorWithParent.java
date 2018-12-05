package epi;
import epi.test_framework.BinaryTreeUtils;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
import epi.test_framework.TestFailure;
import epi.test_framework.TimedExecutor;
public class LowestCommonAncestorWithParent {

  public static BinaryTree<Integer> LCA(BinaryTree<Integer> node0,
                                        BinaryTree<Integer> node1) {
    int d0 = 0, d1 = 0;
    BinaryTree<Integer> it0 = node0, it1 = node1;

    while(it0 != null){
      it0 = it0.parent;
      d0++;
    }

    while(it1 != null){
      it1 = it1.parent;
      d1++;
    }

    int diff = Math.abs(d1 - d0);
    if (d0 < d1){
      for (int i =0; i < diff; i++) node1 = node1.parent;
    } else {
      for (int i =0; i < diff; i++) node0 = node0.parent;
    }

    while (node0 != node1){
      node0 = node0.parent;
      node1 = node1.parent;
    }


    return node0;
  }
  @EpiTest(testDataFile = "lowest_common_ancestor.tsv")
  public static int lcaWrapper(TimedExecutor executor, BinaryTree<Integer> tree,
                               Integer key0, Integer key1) throws Exception {
    BinaryTree<Integer> node0 = BinaryTreeUtils.mustFindNode(tree, key0);
    BinaryTree<Integer> node1 = BinaryTreeUtils.mustFindNode(tree, key1);

    BinaryTree<Integer> result = executor.run(() -> LCA(node0, node1));

    if (result == null) {
      throw new TestFailure("Result can not be null");
    }
    return result.data;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "LowestCommonAncestorWithParent.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
