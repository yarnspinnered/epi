from test_framework import generic_test


def has_two_sum(A, t):
    l,r = 0, len(A) - 1
    while l <= r:
        if A[l] + A[r] == t:
            return True
        elif A[l] + A[r] < t:
            l += 1
        else:
            r -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
