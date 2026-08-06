# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_grp = dummy

        while True:
            kth = prev_grp
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
                
            group_next =  kth.next

            prev = group_next
            curr = prev_grp.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prev_grp.next
            prev_grp.next = kth
            prev_grp = temp

