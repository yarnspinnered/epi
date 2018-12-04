package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
public class IsTreeABst {
  private static class BSTStatus{
    boolean isBST;
    int min;
    int max;

    public BSTStatus(boolean isBST, int min, int max){
      this.isBST = isBST;
      this.min = min;
      this.max = max;
    }
  }
  public static BSTStatus statusChecker(BinaryTreeNode<Integer> u){
    int min = u.data, max = u.data;
    boolean isBST = true;
    if (u.left != null){
      BSTStatus leftStatus = statusChecker(u.left);
      isBST = isBST && leftStatus.isBST && leftStatus.max <= u.data;
      min = Math.min(min, leftStatus.min);
    }
    if (u.right != null){
      BSTStatus rightStatus = statusChecker(u.right);
      isBST = isBST && rightStatus.isBST && rightStatus.min >= u.data;
      max = Math.max(max, rightStatus.max);
    }

    return new BSTStatus(isBST, min,max);
  }
  @EpiTest(testDataFile = "is_tree_a_bst.tsv")

  public static boolean isBinaryTreeBST(BinaryTreeNode<Integer> tree) {
    // TODO - you fill in here.
    if (tree == null){
      return true;
    }
    return statusChecker(tree).isBST;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "IsTreeABst.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
