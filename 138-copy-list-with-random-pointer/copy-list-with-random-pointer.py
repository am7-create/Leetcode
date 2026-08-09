class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        newHead = Node(head.val)

        temp = head
        newTemp = newHead

        while temp.next:
            newTemp.next = Node(temp.next.val)
            temp = temp.next
            newTemp = newTemp.next

        temp = head
        newTemp = newHead

        while temp:
            if temp.random:
                random_temp = head
                random_new = newHead

                while random_temp != temp.random:
                    random_temp = random_temp.next
                    random_new = random_new.next

                newTemp.random = random_new

            temp = temp.next
            newTemp = newTemp.next

        return newHead

