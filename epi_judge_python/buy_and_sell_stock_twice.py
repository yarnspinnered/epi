from test_framework import generic_test


def buy_and_sell_stock_twice(prices):

    #sell_cache records maximum possible profit given that sale happens on day i or earlier
    # buy_cache records maximum possible profit given that buy happens on day i or later
    sell_cache = [0 for x in prices]
    buy_cache = [0 for x in prices]

    profit, small = 0, float('inf')
    for i,x in enumerate(prices):
        sell_cache[i] = max(sell_cache[i - 1] if i > 0 else 0, x - small)
        small = min(small, x)

    profit, big = 0, float('-inf')
    for i in reversed(range(len(prices))):
        x = prices[i]
        buy_cache[i] = max(buy_cache[i + 1] if i < len(prices) - 1 else 0, big - x)
        big = max(big, x)

    res = 0
    for i in range(len(prices)):
        res = max(res, (sell_cache[i - 1] if i > 0 else 0) + buy_cache[i])

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
