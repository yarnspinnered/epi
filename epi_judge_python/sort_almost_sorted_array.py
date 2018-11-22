from test_framework import generic_test
import heapq
import itertools

def sort_approximately_sorted_array(sequence, k):
    res, h = [], []
    it = iter(sequence)
    while True:
        try:
            while len(h) < k:
                heapq.heappush(h, next(it))
            res.append(heapq.heappop(h))
        except StopIteration:
            res += heapq.nsmallest(len(sequence), h)
            break

    return res

def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(sequence, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
