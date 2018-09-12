import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    # TODO - you fill in here.
    for i,x in enumerate(items):
        items[i] = Item(x[0], x[1])
    cache = [[0 for _ in range(len(items))] for _ in range(capacity + 1)]

    for i in range(items[0].weight, capacity + 1):
        cache[i][0] = items[0].value

    for j in range(1, len(items)):
        for i in range(capacity + 1):
            curr_weight = items[j].weight
            curr_val = items[j].value
            if i - curr_weight >= 0:
                cache[i][j] = max(cache[i - curr_weight][j - 1] + curr_val, cache[i][j - 1])
            else:
                # print("i: %d j: %d" % (i,j))
                cache[i][j] = cache[i][j - 1]

    return cache[capacity][len(items) - 1]

optimum_subject_to_capacity([[18, 49], [33, 48], [26, 63], [89, 50], [39, 14], [4, 40], [14, 29], [47, 33], [8, 97], [97, 51], [99, 78], [49, 12], [97, 18], [80, 46], [18, 33], [55, 4], [11, 34], [55, 72], [11, 100], [4, 84], [78, 75], [52, 96], [36, 35], [25, 60], [100, 94], [57, 87], [85, 62], [27, 72], [35, 39], [85, 82], [10, 16], [13, 13], [13, 50], [50, 43], [19, 100], [41, 26], [38, 39], [37, 73], [98, 24], [17, 26], [98, 97], [22, 14], [85, 93], [87, 59], [7, 81], [13, 54], [39, 80], [17, 86], [95, 80], [3, 17], [90, 76], [29, 2], [5, 91], [14, 59], [85, 12], [38, 50], [28, 94], [94, 84], [99, 50], [39, 86], [95, 46], [32, 2], [31, 38], [95, 64], [22, 16], [27, 9], [9, 25], [38, 95], [26, 83], [83, 8], [18, 100], [3, 31], [92, 64], [46, 47], [9, 84], [99, 39], [23, 1], [44, 87], [41, 41], [50, 35], [89, 33], [30, 87], [74, 56], [13, 55], [70, 12], [75, 100], [82, 55], [36, 34], [4, 34], [79, 59], [100, 90], [85, 11], [18, 52], [69, 3], [72, 1], [3, 72], [11, 59], [34, 5], [36, 2], [7, 34], [10, 40], [69, 34], [2, 34], [49, 52], [67, 79], [99, 33], [35, 80], [69, 10], [96, 85], [86, 97], [44, 21], [37, 56], [16, 46], [63, 36], [87, 2], [21, 69], [34, 32], [8, 15], [50, 61], [100, 69], [37, 11], [66, 98], [54, 43], [33, 35], [53, 86], [17, 33], [84, 28], [6, 34], [93, 40], [31, 20], [66, 43], [61, 3], [2, 63], [76, 31], [7, 66], [92, 13], [54, 10], [57, 16], [44, 93], [87, 55], [84, 28], [6, 19], [76, 46], [16, 75], [35, 70], [51, 34], [15, 12], [26, 6], [64, 45], [35, 73], [46, 46], [41, 2], [32, 87], [41, 6], [62, 24], [47, 16], [27, 74], [61, 100]],
                            77)
@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
