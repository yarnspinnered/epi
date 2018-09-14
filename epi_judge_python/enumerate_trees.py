import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from epi_judge_python_solutions.binary_tree_node import BinaryTreeNode

def generate_all_binary_trees(num_nodes):
    if num_nodes == 0:
        return [None]

    res = []
    for i in range(0, num_nodes):
        left = generate_all_binary_trees(i)
        right = generate_all_binary_trees(num_nodes - 1 - i)
        res += [BinaryTreeNode(0, l, r) for l in left for r in right]
    return res


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_trees.py",
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
