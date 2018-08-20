import functools
import math

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount, A):
    # def rotate_one_cycle(offset):
    #     temp = A[offset]
    #     for c in range(1, cycle_length):
    #         idx = (offset + c * rotate_amount) % len(A)
    #         A[idx], temp = temp, A[idx]
    #     A[offset] = temp
    #
    # rotate_amount = rotate_amount % len(A)
    # if rotate_amount == 0:
    #     return
    # num_cycles = math.gcd(rotate_amount, len(A))
    # cycle_length = len(A) // num_cycles
    # for i in range(num_cycles):
    #     rotate_one_cycle(i)
    # return

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    rotate_amount %= len(A)
    reverse(A,0, len(A) - 1)
    reverse(A,0, rotate_amount - 1)
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
