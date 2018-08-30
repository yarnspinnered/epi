from test_framework import generic_test


def zipping_linked_list(L):
    def reverse(u):
        if not u or not u.next:
            return u
        prev, curr = u, u.next
        prev.next = None
        while curr:
            new_curr = curr.next
            curr.next = prev
            curr, prev = new_curr, curr
        return prev

    def find_length(u):
        cnt = 0
        while u:
            cnt += 1
            u = u.next
        return cnt

    if not L or not L.next:
        return L

    length = find_length(L)
    first_half_head, second_half_it = L, L
    for i in range(length//2):
        second_half_it = second_half_it.next
    second_half_head = second_half_it.next
    second_half_it.next = None
    second_half_head = reverse(second_half_head)

    l,r = first_half_head, second_half_head
    while r:
        next_l, next_r = l.next, r.next
        r.next = l.next
        l.next = r
        l,r = next_l, next_r

    return first_half_head
    # def reverse(head):
    #     if not head:
    #         return head
    #     elif not head.next:
    #         return head
    #     else:
    #         curr = head.next
    #         temp = head
    #         head.next = None
    #
    #     while curr:
    #         if curr.next:
    #             future = curr.next
    #             curr.next = temp
    #             curr, temp = future, curr
    #         else:
    #             curr.next = temp
    #             return curr
    #
    # slow = fast = L
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #
    # first_half_head = L
    # second_half_head = slow.next
    # slow.next = None
    # second_half_head = reverse(second_half_head)
    #
    # first_half, second_half = first_half_head, second_half_head
    #
    # while second_half:
    #     second_half.next, first_half.next, second_half = first_half.next, second_half, second_half.next
    #     first_half = first_half.next.next
    #
    # return first_half_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("zip_list.py", 'zip_list.tsv',
                                       zipping_linked_list))
