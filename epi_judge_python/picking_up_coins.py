from test_framework import generic_test
from functools import reduce

def maximum_revenue(coins):
    # TODO - you fill in here.
    cache = [[None for j in range(len(coins) + 1)] for i in  range(len(coins))]
    prefixes = [0]
    for i,c in enumerate(coins):
        prefixes.append(prefixes[-1] + c)

    def helper(i,j):
        if not cache[i][j] is None:
            return cache[i][j]
        if i == j - 1:
            cache[i][j] = coins[i]
            return coins[i]
        pick_right = coins[j - 1] + prefixes[j - 1] - prefixes[i] - helper(i, j - 1)
        pick_left = coins[i] + prefixes[j] - prefixes[i + 1] - helper(i + 1, j)
        if pick_left > pick_right:
            cache[i][j] = pick_left
        else:
            cache[i][j] = pick_right
        return cache[i][j]

    return helper(0, len(coins))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
