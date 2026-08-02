class Solution(object):
    def partition(self, head, x):
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy
        large = large_dummy

        curr  = head

        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next

            else:
                large.next = curr
                large = large.next

            curr = curr.next
        large.next= None
        small.next = large_dummy.next

        return small_dummy.next