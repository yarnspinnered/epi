from test_framework import generic_test
import bisect

def next_permutation(perm):
    perfectly_sorted = True
    to_swap = None
    for i in reversed(range(len(perm) - 1)):
        if perm[i] < perm[i + 1]:
            perfectly_sorted = False
            to_swap = i
            break
    if perfectly_sorted:
        return []

    other_i, other_v = len(perm) - 1, perm[len(perm) - 1]
    for i in reversed(range(to_swap + 1, len(perm))):
        if perm[i] > perm[to_swap]:
            other_i = i
            break
    perm[to_swap], perm[other_i] = perm[other_i], perm[to_swap]


    perm[to_swap + 1:] = reversed(perm[to_swap + 1:])

    return perm
print(next_permutation([1,2,3]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
