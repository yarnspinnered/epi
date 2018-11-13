from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    small, best = float('inf'), 0

    for i,x in enumerate(prices):
        best = max(best, x - small)
        small = min(small, x)
    return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
