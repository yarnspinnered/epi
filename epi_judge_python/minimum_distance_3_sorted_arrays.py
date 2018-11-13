from test_framework import generic_test
import bintrees
import itertools

def find_closest_elements_in_sorted_arrays(sorted_arrays):
    iters = bintrees.RBTree()
    for i,s in enumerate(sorted_arrays):
        it = iter(s)
        v = next(it, None)
        if not v is None:
            iters.insert((v, i), it)
    dist = float('inf')
    while True:
        pair, it = iters.pop_min()
        min_v, arr_i = pair
        max_v = iters.max_key()[0]
        dist = min(dist, max_v - min_v)
        next_v = next(it, None)
        if next_v is None:
            return dist
        else:
            iters.insert((next_v, arr_i), it)
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
