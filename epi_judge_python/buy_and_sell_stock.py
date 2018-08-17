from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    small = float('inf')
    profit = 0
    for i,v in enumerate(prices):
        if v < small:
            small = v
        if v - small > profit:
            profit = v - small
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
