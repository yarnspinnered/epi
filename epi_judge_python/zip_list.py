from test_framework import generic_test


def zipping_linked_list(L):
    def reverse(head):
        if not head:
            return head
        elif not head.next:
            return head
        else:
            curr = head.next
            temp = head
            head.next = None

        while curr:
            if curr.next:
                future = curr.next
                curr.next = temp
                curr, temp = future, curr
            else:
                curr.next = temp
                return curr

    slow = fast = L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first_half_head = L
    second_half_head = slow.next
    slow.next = None
    second_half_head = reverse(second_half_head)

    first_half, second_half = first_half_head, second_half_head

    while second_half:
        second_half.next, first_half.next, second_half = first_half.next, second_half, second_half.next
        first_half = first_half.next.next

    return first_half_head
    # slow = fast = L
    # while fast and fast.next:
    #     slow, fast = slow.next, fast.next.next
    #
    # def reverse_LL(head):
    #     if not head:
    #         return head
    #     elif head.next:
    #         temp = head
    #         curr = head.next
    #         head.next = None
    #     else:
    #         return head
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
    # first_half_head = L
    # second_half_head = slow.next
    # slow.next = None  # Splits the list into two lists.
    #
    #
    #
    # second_half_head = reverse_LL(second_half_head)
    #
    # first_half, second_half = first_half_head, second_half_head
    #
    # while second_half:
    #     first_half.next, second_half.next, second_half = second_half, first_half.next, second_half.next
    #     first_half = first_half.next.next
    #
    # return first_half_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("zip_list.py", 'zip_list.tsv',
                                       zipping_linked_list))
