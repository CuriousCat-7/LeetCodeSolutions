# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        r = []
        if root == None:
            return r
        q.append(root)
        q.append(None)
        while True:
            sub = []
            while True:
                root = q.pop(0)
                if root == None:
                    q.append(None)
                    r.append(sub)
                    break
                sub.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)                    
            if len(q) <= 1:
                break
        return r


