from test_framework import generic_test
import heapq

def sort_k_increasing_decreasing_array(A):
    sorted_subarrs = []
    curr = []
    sorted_subarrs.append(curr)
    increasing = True

    for i,x in enumerate(A):
        if i == 0:
            curr.append(x)
            continue
        if (increasing and A[i - 1] <= x) or (not increasing and A[i - 1] >= x):
            curr.append(x)
        else:
            if not increasing:
                curr.reverse()
            increasing = not increasing
            curr = [x]
            sorted_subarrs.append(curr)
    if not increasing:
        curr.reverse()
    res = heapq.merge(*sorted_subarrs)
    return list(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
