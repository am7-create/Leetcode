# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorderIndexMap = {}

        for i in range(len(inorder)):
            inorderIndexMap[inorder[i]] = i


        return self.splitTree(
            preorder,
            inorderIndexMap,
            rootIndex = 0,
            left = 0,
            right = len(inorder) - 1
        )
    def splitTree(self,preorder,inorderIndexMap,rootIndex,left,right):

        if left > right:
            return None


        root = TreeNode(preorder[rootIndex])

        mid = inorderIndexMap[preorder[rootIndex]]

        if mid > left:
            root.left = self.splitTree(
                preorder,
                inorderIndexMap,
                rootIndex + 1,
                left,
                mid - 1
            )
        if mid < right:
            root.right = self.splitTree(
                preorder,
                inorderIndexMap,
                rootIndex + (mid - left) + 1,
                mid + 1,
                right
            )

        return root