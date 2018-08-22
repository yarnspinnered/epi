from test_framework import generic_test
import functools

def find_biggest_n_minus_one_product(A):
    prefix = [1]*len(A)
    suffix = [1]*len(A)

    for i in range(1, len(A)):
        prefix[i] = A[i - 1] * prefix[i-1]

    for i in range(len(A) - 2,-1,-1):
        suffix[i] = A[i + 1] * suffix[i + 1]

    max_val = float('-inf')

    for i in range(len(A)):
        if prefix[i] * suffix[i] > max_val:
            max_val = prefix[i] * suffix[i]

    return max_val
    # def pdt_without_one_index(arr, skip):
    #     tot = 1
    #     for i,x in enumerate(arr):
    #         if i != skip:
    #             tot *= x
    #     return tot
    #
    # neg_cnt = len(list(filter(lambda x: x < 0, A)))
    # smallest_neg = len(A)
    # smallest_pos = len(A)
    #
    # for i,x in enumerate(A):
    #     if x < 0:
    #         if smallest_neg == len(A):
    #             smallest_neg = i
    #         else:
    #             if x > A[smallest_neg]:
    #                 smallest_neg = i
    #     elif x >= 0:
    #         if smallest_pos == len(A):
    #             smallest_pos = i
    #         else:
    #             if x < A[smallest_pos]:
    #                 smallest_pos = i
    #
    # if neg_cnt % 2 == 0:
    #     return pdt_without_one_index(A, smallest_pos)
    #
    # else:
    #     return pdt_without_one_index(A, smallest_neg)
    #


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_product_all_but_one.py",
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
