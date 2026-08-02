# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        curr = root

        while curr is not None:
            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right

            else:
                ip = curr.left

                while ip.right is not None and ip.right != curr:
                    ip = ip.right


                if ip.right is None:
                    ip.right = curr
                    curr = curr.left

                else:
                    ip.right = None
                    ans.append(curr.val)
                    curr = curr.right

        return ans

        ans = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)


        inorder(root)
        return ans