from test_framework import generic_test


def even_odd_merge(L):
    if not L or not L.next:
        return L

    even = L
    odd_start = odd = L.next
    even_end = None
    while True:
        if not odd:
            break
        even.next = odd.next
        if not even.next:
            even_end = even
        even = even.next

        if not even:
            break
        odd.next = even.next
        odd = odd.next

    if even:
        even.next = odd_start
    else:
        even_end.next = odd_start
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
