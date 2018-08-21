from test_framework import generic_test
import heapq
from collections import namedtuple

def calculate_bonus(productivity):
    tickets = [1]*len(productivity)

    for i in range(1, len(productivity)):
        if productivity[i-1] < productivity[i]:
            tickets[i] = tickets[i-1] + 1

    for i in reversed(range(len(productivity)-1)):
        if productivity[i] > productivity[i+1]:
            tickets[i] = max(tickets[i], tickets[i+1] + 1)

    # tickets = [1]*len(productivity)
    # e = namedtuple("Employee", ["productivity", "position"])
    # h = [e(x,i) for i,x in enumerate(productivity)]
    # heapq.heapify(h)
    #
    # while h:
    #     curr = heapq.heappop(h)
    #
    #     i = curr.position
    #     x = curr.productivity
    #
    #     if i > 0 and productivity[i - 1] < x:
    #         tickets[i] = max(tickets[i], tickets[i-1] + 1)
    #     if i < len(productivity) - 1 and productivity[i+1] < x:
    #         tickets[i] = max(tickets[i], tickets[i+1] + 1)

    return sum(tickets)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bonus.py", 'bonus.tsv',
                                       calculate_bonus))
