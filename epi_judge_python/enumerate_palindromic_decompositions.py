from test_framework import generic_test


def palindrome_decompositions(input):
    def helper(offset, state):
        if offset == len(input):
            res.append(list(state))
            return

        for i in range(offset + 1, len(input) + 1):
            candidate = input[offset:i]
            if candidate[::-1] == candidate:
                helper(i, state + [candidate])

    res = []
    helper(0, [])
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
