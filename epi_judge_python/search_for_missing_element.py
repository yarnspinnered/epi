import collections
import functools
import math
from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A):
    a_xor = functools.reduce(lambda x,z: x ^ z, A)
    n_xor = functools.reduce(lambda x,z: x ^ z, range(len(A)))

    h = a_xor ^ n_xor
    first_set_bit_in_h = (h | (h - 1)) ^ (h - 1)

    miss_or_dup = 0
    for i,x in enumerate(A):
        if (x & first_set_bit_in_h):
            miss_or_dup ^= x
        if i & first_set_bit_in_h:
            miss_or_dup ^= i

    if miss_or_dup in A:
        return DuplicateAndMissing(miss_or_dup, miss_or_dup ^ h)
    else:
        return DuplicateAndMissing(miss_or_dup ^ h , miss_or_dup)

find_duplicate_missing([0,0])
def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
