from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    if not sorted_arrays:
        return sorted_arrays

    heap = []
    for i, arr in enumerate(sorted_arrays):
        if len(arr) > 0:
            heap.append((arr.pop(0), i))
    heapq.heapify(heap)

    res = []
    while heap:
        smallest = heapq.heappop(heap)
        corresp_arr = sorted_arrays[smallest[1]]
        if len(corresp_arr) > 0:
            heapq.heappush(heap, (corresp_arr.pop(0), smallest[1]))
        res.append(smallest[0])



    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
