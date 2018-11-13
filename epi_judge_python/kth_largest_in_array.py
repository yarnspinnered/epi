from test_framework import generic_test
import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def partition_around_pivot(l,r,p_i):
        A[r], A[p_i] = A[p_i], A[r]
        new_p_i = l
        for i in range(l, r):
            if A[i] >= A[r]:
                A[new_p_i], A[i] = A[i], A[new_p_i]
                new_p_i += 1
        A[r], A[new_p_i] = A[new_p_i], A[r]
        return new_p_i

    l, r = 0, len(A) - 1
    while l <= r:
        p = random.randint(l,r)
        next_p = partition_around_pivot(l,r,p)

        if next_p == k - 1:
            return A[next_p]
        elif next_p > k - 1:
            r = next_p - 1
        else:
            l = next_p + 1
# print(find_kth_largest(3, [3,2,1,5,4]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
