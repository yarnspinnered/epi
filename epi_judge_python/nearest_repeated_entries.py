from test_framework import generic_test
from collections import defaultdict

def find_nearest_repetition(paragraph):
    d = defaultdict(lambda: float('-inf'))
    dist = float('inf')
    for i,w in enumerate(paragraph):
        dist = min(i - d[w], dist)
        d[w] = i
    return -1 if dist == float('inf') else dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
