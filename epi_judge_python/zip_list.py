from test_framework import generic_test


def zipping_linked_list(L):
    def reverse(u):
        if not u or not u.next:
            return u
        prev = u
        curr = u.next
        u.next = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def find_length(u):
        length = 0
        while u:
            length += 1
            u = u.next
        return length
    right_half_start = L
    for i in range(find_length(L)//2):
        right_half_start = right_half_start.next
    right_half_start.next, right_half_start = None, right_half_start.next

    left_half_start = L
    right_half_start = reverse(right_half_start)

    l = left_half_start
    r = right_half_start
    while r:
        next_l, next_r = l.next, r.next
        l.next, r.next = r, l.next
        r,l = next_r, next_l
    return left_half_start
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
