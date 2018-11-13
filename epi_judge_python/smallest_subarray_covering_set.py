import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))
from collections import Counter

def find_smallest_subarray_covering_set(paragraph, keywords):
    def get_length(sub):
        return sub.end - sub.start

    l =  0
    d = Counter()
    shortest = Subarray(0, len(paragraph))
    for r in range(1, len(paragraph) + 1):
        w = paragraph[r - 1]
        if not w in keywords:
            continue
        d[w] += 1
        while len(d) == len(keywords):
            candidate = Subarray(l, r)
            if get_length(shortest) > get_length(candidate):
                shortest = candidate
            l_w =paragraph[l]
            if l_w in d:
                d[l_w] -= 1
                if d[l_w] == 0:
                    d.pop(l_w)
            l +=  1
    return Subarray(shortest.start, shortest.end - 1)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
