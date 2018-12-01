from test_framework import generic_test
from itertools import accumulate

def find_longest_subarray_less_equal_k(A, k):
    P, Q = [], [float('inf') for _ in range(len(A))]
    P = list(accumulate(A))
    Q[-1] = P[-1]
    for i in reversed(range(len(A) -1)):
        Q[i] = min(P[i], Q[i + 1])

    if P[-1] <= k:
        return len(A)

    a,b = 0,0
    max_len = 0
    while a < len(A) and b < len(A):
        if (Q[b] - P[a - 1] if a > 0 else Q[b]) <= k:
            max_len = max(max_len, b - a + 1)
            b += 1
        else:
            a += 1

    return max_len
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_sum_constraint.py",
            'longest_subarray_with_sum_constraint.tsv',
            find_longest_subarray_less_equal_k))
