package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
public class IsTreeBalanced {
  private static class Pair {
    final boolean balanced;
    final int height;
    public Pair(boolean balanced, int height){
      this.balanced = balanced;
      this.height = height;
    }
  }

  public static Pair recursiveCheck(BinaryTreeNode<Integer> tree){
    if (tree == null){
      return new Pair(true, 0);
    }
    Pair left = recursiveCheck(tree.left);
    Pair right = recursiveCheck(tree.right);

    return new Pair(left.balanced && right.balanced && Math.abs(left.height - right.height) <= 1,
            Math.max(left.height, right.height) + 1 );
  }

  @EpiTest(testDataFile = "is_tree_balanced.tsv")
  public static boolean isBalanced(BinaryTreeNode<Integer> tree) {

    return recursiveCheck(tree).balanced;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "IsTreeBalanced.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
