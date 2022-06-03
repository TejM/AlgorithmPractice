# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_value = p.val
        q_value = q.val
        root_value = root.val
        
        if p_value < root_value and q_value < root_value:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_value > root_value and q_value > root_value:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root  

# Time Complexity: O(log N)
# Space Complexity: O(1)
