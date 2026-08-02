# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorderIndexMap = {}

        for i in range(len(inorder)):
            inorderIndexMap[inorder[i]] = i

        self.postIndex = len(postorder) - 1

        def helper(left,right):
            if left > right:
                return None

            rootVal = postorder[self.postIndex]
            self.postIndex -= 1

            root = TreeNode(rootVal)

            mid = inorderIndexMap[rootVal]

            root.right = helper(mid + 1, right)

            root.left = helper(left, mid -1)

            return root

        return helper(0, len(inorder) - 1)