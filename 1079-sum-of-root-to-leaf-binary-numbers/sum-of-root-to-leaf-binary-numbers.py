# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def get_all_binary(root):
            if root is None:
                return ([], 0)
            
            if root.left is None and root.right is None:
                return ([str(root.val)], root.val)
            
            all_strings = get_all_binary(root.left)[0] + get_all_binary(root.right)[0]
            answer = []
            curr_sum = 0
            for string in all_strings:
                answer.append(str(root.val) + string)
                curr_sum += int(answer[-1], 2)
            
            return (answer, curr_sum)
        return get_all_binary(root)[1]
