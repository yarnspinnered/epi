from test_framework import generic_test
from random import randint
from collections import deque

def majority_search(stream):

    def partition(l, r, p_i):
        p_x = arr[p_i]
        arr[r], arr[p_i] = arr[p_i], arr[r]
        clean = l
        for i in range(l,r):
            if arr[i] < p_x:
                arr[clean], arr[i] = arr[i], arr[clean]
                clean += 1
        arr[clean],arr[r] = arr[r], arr[clean]
        return clean

    def select(l, r, k):
        p_i = partition(l,r, randint(l,r))
        if p_i == k:
            return arr[p_i]
        elif p_i < k:
            return select(p_i + 1, r, k)
        else:
            return select(l, p_i - 1, k)

    arr = list(stream)

    return select(0, len(arr) - 1, len(arr)//2)

def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
