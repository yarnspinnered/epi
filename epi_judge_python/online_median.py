from test_framework import generic_test
import heapq

def online_median(sequence):
    l, r, res = [], [], []

    for i,x in enumerate(sequence, 1):
        l_wanted_size = i // 2
        l_big, r_small = -l[0] if len(l) > 0 else float('-inf'), r[0] if len(r) > 0 else float('inf')
        if x < l_big:
            heapq.heappush(l, -x)
        else:
            heapq.heappush(r, x)
        if len(l) > l_wanted_size:
            move_l = heapq.heappop(l)
            heapq.heappush(r, -move_l)
        elif len(l) < l_wanted_size:
            move_r = heapq.heappop(r)
            heapq.heappush(l, -move_r)
        res.append(r[0] if i % 2 == 1 else (-l[0] + r[0])/2)
    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
