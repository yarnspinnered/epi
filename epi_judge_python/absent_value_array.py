from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools

def find_missing_element(stream):
    bit_arr = [0 for x in range(2**16)]
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        bit_arr[x >> 16] += 1

    for i,x in enumerate(bit_arr):
        if x < 2 ** 16:
            candidate = i
            break

    bit_arr = [0 for x in range(2**16)]
    for x in stream_copy:
        if x >> 16 == candidate:
            bit_arr[0x0000ffff & x] = 1

    for i,x in enumerate(bit_arr):
        if x == 0:
            return i
    return 0


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
