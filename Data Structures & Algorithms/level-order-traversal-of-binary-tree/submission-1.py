# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        newList = []

        if not root:
            return newList

        queue = deque([root])
        while queue:
            q = len(queue)
            level = []
            while q:
                elem = queue.popleft()
                level.append(elem.val)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)

                q -= 1
            newList.append(level)
        return newList








            

    
        
