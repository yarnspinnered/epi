import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    def walk(u):
        if not u:
            return
        walk(u.left)
        if l <= u.data <= r:
            res.append(u.data)
        walk(u.right)

    l,r  = interval
    if not tree:
        return []
    if tree.data < l:
        return range_lookup_in_bst(tree.right, interval)
    elif tree.data > r:
        return range_lookup_in_bst(tree.left, interval)
    else:
        res = []
        walk(tree)

    return res


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
