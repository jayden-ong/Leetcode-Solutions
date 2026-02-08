# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(root:Optional[TreeNode]) -> int:
            if root is None:
                return 0
            return max(get_depth(root.left), get_depth(root.right)) + 1
        
        if root is None:
            return True
        return abs(get_depth(root.left) - get_depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)