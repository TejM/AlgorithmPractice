# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and (root.left != None or root.right != None):
            left = root.left
            right = root.right
            root.left = self.invertTree(right)
            root.right = self.invertTree(left)
        return root

# Time complexity O(log(N))
# Space complexity O(N)
