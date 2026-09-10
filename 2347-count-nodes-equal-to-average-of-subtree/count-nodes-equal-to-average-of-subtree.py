# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def solve(root):
            if root.left is None and root.right is None:
                return (1, root.val, 1)
            
            right_answer = right_sum = right_children = 0
            if root.right is not None:
                right_answer, right_sum, right_children = solve(root.right)
            
            left_answer = left_sum = left_children = 0
            if root.left is not None:
                left_answer, left_sum, left_children = solve(root.left)
            
            total_children = right_children + left_children + 1
            curr_answer = right_answer + left_answer
            curr_sum = right_sum + left_sum + root.val
            if curr_sum // total_children == root.val:
                curr_answer += 1
            return (curr_answer, curr_sum, total_children)
        return solve(root)[0]
