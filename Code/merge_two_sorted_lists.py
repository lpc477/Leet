class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    head = result = ListNode(0)
    while l1 and l2:
        if l1.val > l2.val:
            result.next = l2
            l2 = l2.next
        else:
            result.next = l1
            l1 = l1.next
        result = result.next
    if l1:
        result.next = l1
    elif l2:
        result.next = l2
    return head.next
