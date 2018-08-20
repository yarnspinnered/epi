import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from queue_with_max import QueueWithMax
# from epi_judge_python_solutions.queue_with_max_using_deque import QueueWithMax
class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __eq__(self, other):
        return self.volume == other.volume and self.time == other.time

    def __repr__(self):
        return f"time: {self.time} volume: {self.volume}"
def calculate_traffic_volumes(A, w):
    q = QueueWithMax()
    res = []
    for i,x in enumerate(A):

        try:
            # print("Boolean: ",  q[0].time + w < x.time)
            while q.q[0].time + w < x.time:
                q.dequeue()
            q_max = q.max()
        except:
            q_max = TrafficElement(0,0)
        q.enqueue(x)
        if q_max > x:
            res.append(TrafficElement(x.time, q_max.volume))
        else:
            res.append(TrafficElement(x.time, x.volume))



    return res


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_of_sliding_window.py",
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
