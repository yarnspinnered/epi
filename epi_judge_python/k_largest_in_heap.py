from test_framework import generic_test, test_utils
import heapq

def k_largest_in_binary_heap(A, k):
    def getChild(i):
        res = []
        if i * 2 + 1 < len(A):
            res.append((-A[i*2 + 1], i * 2 + 1))
        if i * 2 + 2 < len(A):
            res.append((-A[i * 2 + 2], i * 2 + 2))
        return res

    h = [(-A[0], 0)]
    res = []
    while len(res) < k:
        x, i = heapq.heappop(h)
        children = getChild(i)
        for c in children:
            heapq.heappush(h, c)
        res.append(-x)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
