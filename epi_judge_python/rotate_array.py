import functools
import math

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount, A):
    # num_cycles = math.gcd(rotate_amount, len(A))
    # cycle_length = len(A) // num_cycles
    #
    # for i in range(num_cycles):
    #     temp = A[i]
    #     for j in range(cycle_length):
    #         dst_pos = (i + (j+1) * rotate_amount) % len(A)
    #         A[dst_pos], temp = temp, A[dst_pos]
    #
    def reverse(A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start, end = start + 1, end - 1
    rotate_amount %= len(A)
    reverse(A, 0, len(A) - 1)
    reverse(A, 0, rotate_amount - 1)
    reverse(A, rotate_amount, len(A) - 1)

@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rotate_array.py", 'rotate_array.tsv',
                                       rotate_array_wrapper))
