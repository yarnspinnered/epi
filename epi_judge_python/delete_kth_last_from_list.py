from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    front = L
    back = L
    for i in range(k):
        back = back.next

    prev = None
    while not back is None:
        prev = front
        front = front.next
        back = back.next

    if prev:
        prev.next = prev.next.next
    else:
        L = L.next



    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
