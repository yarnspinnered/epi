from test_framework import generic_test


def maximum_revenue(coins):
    # TODO - you fill in here.
    cache = [[float('inf') for j in range(len(coins) + 1)] for i in  range(len(coins))]

    for i in range(len(coins)):
        cache[i][i + 1] = coins[i]

    for offset in range(2,len(coins) + 1):
        for i in range(len(coins) - offset + 1):
            cache[i][i + offset] = sum(coins[i:i+offset]) - min(cache[i+1][i+offset], cache[i][i + offset - 1])

    return cache[0][len(coins)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
