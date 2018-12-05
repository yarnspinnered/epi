package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;
public class ReverseSublist {
  @EpiTest(testDataFile = "reverse_sublist.tsv")

  public static ListNode<Integer> reverseSublist(ListNode<Integer> L, int start,
                                                 int finish) {
    if (start == finish) return L;

    ListNode<Integer> l = new ListNode<>(0,L), dummyHead = l;
    for (int i = 1; i < start; i ++){
      l = l.next;
    }

    ListNode<Integer> subIter = l.next;
    while (start++ < finish){
      ListNode<Integer> tmp = subIter.next;
      subIter.next = tmp.next;
      tmp.next = l.next;
      l.next = tmp;

    }

    return dummyHead.next;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "ReverseSublist.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
