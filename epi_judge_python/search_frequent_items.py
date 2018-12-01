from test_framework import generic_test, test_utils
from collections import defaultdict, Counter
from itertools import tee
# Finds the candidates which may occur > n / k times.
def search_frequent_items(k, stream):
    stream, stream1 = tee(stream, 2)
    d = Counter()
    n = 0
    for x in stream:
        n += 1
        d[x] += 1
        if len(d) > k:
            for it in d:
                d[it] -= 1
            d = +d

    for kv in d:
        d[kv] = 0

    for x in stream1:
        if x in d:
            d[x] += 1

    return [x for x in d if d[x] > n/k]
# print(search_frequent_items(3, ["b", "c", "b", "b", "b", "d", "d", "e", "d", "d", "d", "e", "e", "e"]))

def search_frequent_items_wrapper(k, stream):
    return search_frequent_items(k, iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_frequent_items.py", "search_frequent_items.tsv",
            search_frequent_items_wrapper, test_utils.unordered_compare))
