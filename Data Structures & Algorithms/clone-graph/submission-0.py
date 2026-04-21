"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        visited = set()
        hashmap = {}

        def dfs(node):
            if node in visited:
                return 

            visited.add(node)
            hashmap[node] = Node(node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

            return

        dfs(node)

        for old_node, new_node in hashmap.items():
            for neighbor in old_node.neighbors:
                new_neighbor = hashmap[neighbor]
                new_node.neighbors.append(new_neighbor)

        return hashmap[node]




