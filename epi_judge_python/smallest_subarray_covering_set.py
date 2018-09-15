import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    d = {}.fromkeys(keywords, 0)
    remaining_cnt = len(keywords)
    left = 0
    shortest = Subarray(0, len(paragraph) - 1)

    for right, w in enumerate(paragraph):

        if w in d:
            if d[w] == 0:
                remaining_cnt -= 1
            d[w] += 1
        while remaining_cnt == 0:
            if right - left  < shortest.end - shortest.start:
                shortest = Subarray(left, right)
            left_w = paragraph[left]
            if left_w in d:
                d[left_w] -= 1
                if d[left_w] == 0:
                    remaining_cnt += 1
            left += 1

    return shortest


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
