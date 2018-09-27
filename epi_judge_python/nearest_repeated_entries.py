from test_framework import generic_test


def find_nearest_repetition(paragraph):
    d = {}
    for i,w in enumerate(paragraph):
        if w in d:
            prev, closest_so_far = d[w]
            d[w] = (i, min(closest_so_far, i - prev))
        else:
            d[w] = (i, float('inf'))

    res = float('inf')
    for k,v in d.items():
        res = min(smallest for k,(_, smallest) in d.items())
    return -1 if res == float('inf') else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
