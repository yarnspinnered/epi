from test_framework import generic_test


def h_index(citations):
    citations.sort()
    res = 0
    for i,c in enumerate(citations):
        if c >= len(citations) - i:
           res = max(res, len(citations) - i)
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
