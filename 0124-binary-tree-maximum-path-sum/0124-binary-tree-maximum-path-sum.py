class Solution(object):
    def maxPathSum(self, root):
        self.answer = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))

            current_sum = left + node.val + right

            self.answer = max(self.answer,current_sum)

            return node.val + max(left,right)

        dfs(root)

        return self.answer