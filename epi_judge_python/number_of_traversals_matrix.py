from test_framework import generic_test


def number_of_ways(n, m):
    def number_of_ways(n, m):
        up = [0 for j in range(m)]
        print(up)
        curr = 0
        for i in range(n):
            if i == 0:
                left = 1
            else:
                left = 0
            for j in range(m):
                curr = left + up[j]
                up[j] = curr
                left = curr

        return up[-1]
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
