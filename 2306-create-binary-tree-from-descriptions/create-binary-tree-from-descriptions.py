# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Want to map each parent to all of its children
        parent_to_children = {}
        children = set()
        for parent, child, isLeft in descriptions:
            if parent in parent_to_children:
                parent_to_children[parent].append((child, isLeft))
            else:
                parent_to_children[parent] = [(child, isLeft)]
            
            children.add(child)
        
        root_val = None
        for parent, _, _ in descriptions:
            if parent not in children:
                root_val = parent
                break
        
        def build_tree(root_val):
            root = TreeNode(root_val, None, None)
            if root_val in parent_to_children:
                all_children = parent_to_children[root_val]
                for child_val, isLeft in all_children:
                    if isLeft:
                        root.left = build_tree(child_val)
                    else:
                        root.right = build_tree(child_val)

            return root
        
        return build_tree(root_val)