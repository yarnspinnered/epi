import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0,
                                               possible_anc_or_desc_1, middle):
    def find(s,t):
        while s and s is not t:
            if s.data < t.data:
                s = s.right
            else:
                s = s.left
        return s is t

    search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1
    while  search_0 is not possible_anc_or_desc_1 \
            and search_1 is not possible_anc_or_desc_0 \
            and not search_0 is middle \
            and not search_1 is middle and (search_0 or search_1):
        if search_0:
            search_0 = search_0.left if search_0.data > middle.data else search_0.right
        if search_1:
            search_1 = search_1.left if search_1.data > middle.data else search_1.right

    if not (search_0 is middle or search_1 is middle) or search_0 is possible_anc_or_desc_1 \
        or search_1 is possible_anc_or_desc_0:
        return False
    return find(middle, possible_anc_or_desc_1 if search_0 is middle else possible_anc_or_desc_0)


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
        executor, tree, possible_anc_or_desc_0, possible_anc_or_desc_1,
        middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
