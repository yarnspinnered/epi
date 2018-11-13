import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import deque

def lca(tree, node0, node1):
    def helper(u):
        if not u:
            return (0, None)
        l_cnt, l_ancestor = helper(u.left)
        r_cnt, r_ancestor = helper(u.right)

        if l_cnt == 2:
            return (l_cnt, l_ancestor)
        elif r_cnt == 2:
            return (r_cnt, r_ancestor)
        num_nodes = l_cnt + r_cnt + (node0, node1).count(u)
        return (num_nodes, u if num_nodes == 2 else None)
    return helper(tree)[1]



@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
