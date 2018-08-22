import collections

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A):
    if not A:
        return A
    start,end, best_start, best_end = 0, 0, 0, 0

    for i in range(1,len(A)):
        if A[i] > A[i - 1]:
            end = i
            if end - start > best_end - best_start:
                best_start = start
                best_end = end
        else:
            start = i
            end = i

    return Subarray(best_start, best_end)
    # def increasing(A,i):
    #     return A[i] > A[i-1]
    # best_start = 0
    # best_end = 1
    # start = 0
    # end = 1
    #
    # for i in range(1, len(A)):
    #
    #     if increasing(A,i):
    #         end += 1
    #     else:
    #         if end - start > best_end - best_start:
    #             best_end = end
    #             best_start = start
    #         start = i
    #         end = i + 1
    # if end - start > best_end - best_start:
    #     best_end = end
    #     best_start = start
    #
    # return Subarray(best_start, best_end - 1)


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_increasing_subarray.py",
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
