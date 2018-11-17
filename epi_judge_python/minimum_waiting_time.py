from test_framework import generic_test
import functools

def minimum_total_waiting_time(service_times):
    service_times.sort()
    res = 0
    prefix = 0
    for i in range(len(service_times)):
        res += prefix
        prefix += service_times[i]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
