from test_framework import generic_test
import heapq
import itertools

def sort_approximately_sorted_array(sequence, k):
    heap = []
    heap_iter = iter(sequence)

    for x in itertools.islice(heap_iter, k):
        heapq.heappush(heap, x)

    res = []
    for x in heap_iter:
        heapq.heappush(heap, x)
        res.append(heapq.heappop(heap))

    while heap:
        res.append(heapq.heappop(heap))

    return res

def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(sequence, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
