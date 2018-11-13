from test_framework import generic_test, test_utils
import itertools

def permutations(A):
    def helper(offset, state):
        if offset == len(A):
            res.append(list(state))
            return
        for j in range(offset, len(A)):
            state[offset], state[j] = state[j], state[offset]
            helper(offset + 1, state)
            state[j], state[offset] = state[offset], state[j]
    res = []
    helper(0, A[:])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
