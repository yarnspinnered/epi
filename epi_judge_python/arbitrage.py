from test_framework import generic_test
import math

def is_arbitrage_exist(graph):
    def relax_edges(cost):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i == j:
                    continue
                cost[j] = min(cost[j], cost[i] - math.log(graph[i][j]))

    def candidate_currency(x):
        cost = {i:float('inf') for i in range(len(graph))}
        cost[x] = 0
        for i in range(len(graph) - 1):
            relax_edges(cost)
        old_cost = cost.copy()
        relax_edges(cost)
        return old_cost != cost



    return candidate_currency(0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("arbitrage.py", "arbitrage.tsv",
                                       is_arbitrage_exist))
