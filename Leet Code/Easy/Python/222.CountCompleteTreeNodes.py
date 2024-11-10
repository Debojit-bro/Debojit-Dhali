# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None: return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
root = TreeNode(2, TreeNode(5), TreeNode(4))

print(Solution().countNodes(root))