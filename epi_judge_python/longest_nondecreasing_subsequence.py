from test_framework import generic_test
from operator import itemgetter

def longest_nondecreasing_subsequence_length(A):
    cache = [1]

    for i in range(1, len(A)):
        longest = 1
        for j in range(i):
            if A[j] <= A[i]:
                longest = max(longest, cache[j] + 1)
        cache.append(longest)

    return max(cache)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
