import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    task_durations.sort()
    res = []
    l,r = 0, len(task_durations) - 1
    while l < r:
        res.append(PairedTasks(task_durations[l], task_durations[r]))
        l += 1
        r -= 1
    if l == r:
        res.append((task_durations[l],))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))
