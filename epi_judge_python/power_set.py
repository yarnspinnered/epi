from test_framework import generic_test, test_utils


def generate_power_set(S):
    def helper(i, state_so_far):
        if i == len(S):
            res.append(list(state_so_far))
            return
        else:
            if_i_included = helper(i + 1, state_so_far + [S[i]])
            if_i_not_included = helper(i + 1, state_so_far)
    res= []
    helper(0, [])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
