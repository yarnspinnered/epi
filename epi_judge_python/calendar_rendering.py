import collections
import functools
import bisect

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    endpoints = [x for e in A for x in ((e.start, False), (e.finish, True)) ]
    endpoints.sort()

    curr = 0
    max_events = 0
    for end in endpoints:
        if not end[1]:
            curr += 1
            max_events = max(max_events, curr)
        else:
            curr -= 1
    return max_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
