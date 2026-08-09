# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteNode(self,node):
        node.val = node.next.val
        node.next = node.next.next