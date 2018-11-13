from test_framework import generic_test
import bintrees

def generate_first_k_a_b_sqrt2(k):
    tree = bintrees.RBTree()
    tree.insert(0,(0,0))
    res = []

    def f(a,b):
        return a + b * 2 ** 0.5
    while len(res) < k:
        v, pair = tree.pop_min()
        res.append(v)
        tree.insert(f(pair[0]  + 1,pair[1]), (pair[0] + 1, pair[1]))
        tree.insert(f(pair[0] ,pair[1]+ 1), (pair[0] , pair[1]+ 1))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
