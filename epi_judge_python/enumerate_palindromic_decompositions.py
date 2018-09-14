from test_framework import generic_test


def palindrome_decompositions(input):
    def helper(offset):
        if offset in cache:
            return cache[offset]
        res = []
        for i in range(offset - 1, -1, -1):
            if input[i:offset] == input[i:offset][::-1]:
                prev = helper(i)
                if not prev:
                    res.append([input[i:offset]])
                res += [e + [input[i:offset]] for e in prev]
        cache[offset] = res
        return res

    cache = {0:[]}

    return helper(len(input))


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
