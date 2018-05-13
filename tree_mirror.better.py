class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left, right):
            if not left and not right:
                return True
            elif not (left and right):
                return False
            
            if left.val == right.val:
                return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            else:
                return False
        if not root:
            return True
        else:
            return isMirror(root.left, root.right)

