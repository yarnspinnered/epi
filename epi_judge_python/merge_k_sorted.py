import heapq

def merge_k_sorted_arrays(input):
    heap = []
    for i, arr in enumerate(input):
        arr.reverse()
        if arr:
            heapq.heappush(heap, (arr.pop(), i))

    res = []
    while heap:
        x, source_arr = heapq.heappop(heap)
        res.append(x)
        if input[source_arr]:
            heapq.heappush(heap, (input[source_arr].pop(), source_arr))

    return res
