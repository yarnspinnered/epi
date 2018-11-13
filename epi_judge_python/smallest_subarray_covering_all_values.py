import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    kw_pos = {k : i for i,k in enumerate(keywords)}
    kw_latest = {k: -1 for k in keywords}
    kw_subarr = {k : float('inf') for k in keywords}
    res = Subarray(0, len(paragraph))

    for r,w in enumerate(paragraph):
        if w in kw_pos:
            kw_latest[w] = r
            pos = kw_pos[w]
            if pos == 0:
                kw_subarr[w] = 1
            else:
                prev = keywords[pos - 1]
                if kw_subarr[prev] != float('inf'):
                    kw_subarr[w] = kw_subarr[prev] + (r - kw_latest[prev])
            if pos == len(keywords) - 1 and res.end - res.start  + 1> kw_subarr[w]:
                res = Subarray(r - kw_subarr[w] + 1, r )
    return res


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
