# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        val = root.val

        def dfs(root):
            nonlocal cnt, val
            if not root:
                return  
            dfs(root.left)
            cnt += 1
            if cnt == k:
                val = root.val
            dfs(root.right)

        dfs(root)
        return val

            
            

