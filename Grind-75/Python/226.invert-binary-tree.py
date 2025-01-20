# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root


        newRoot = root

        nodeStack = []
        nodeStack.append(newRoot)

        while nodeStack:
            node = nodeStack[0]

            tempNode = node.right
            node.right = node.left
            node.left = tempNode

            if node.left:
                nodeStack.append(node.left)
            if node.right:
                nodeStack.append(node.right)

            nodeStack.pop(0)
        return newRoot
        

# @leet end
