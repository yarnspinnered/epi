from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    first_profit = [0 for x in prices]
    small = float('inf')

    for i, p in enumerate(prices):
        if p - small > first_profit[i]:
            first_profit[i] = p - small
        elif i > 0 :
            first_profit[i] = first_profit[i - 1]
        small = min(small, p)

    second_profit = [0 for x in prices]
    big = prices[-1]
    for i in reversed(range(len(prices) - 1)):
        p = prices[i]
        if big - p > second_profit[i + 1]:
            second_profit[i] = big - p
        else:
            second_profit[i] = second_profit[i + 1]
        big = max(big, p)

    return max(first_profit[-1], second_profit[0], max(first_profit[i] + second_profit[i + 1] for i in range(len(prices) - 1)))

buy_and_sell_stock_twice([12,11,13,9,12,8,14,13,15])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
