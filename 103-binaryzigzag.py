# mine
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        right_first = False
        self.l = []
        def help(stack, right_first):
            if not stack:
                return
            n_stack = []
            sub = []
            while True:
                try:
                    a = stack.pop()
                except:
                    self.l.append(sub)
                    break
                sub.append(a.val)
                if right_first:
                    if a.right:
                        n_stack.append(a.right)
                    if a.left:
                        n_stack.append(a.left)
                else:
                    if a.left:
                        n_stack.append(a.left)
                    if a.right:
                        n_stack.append(a.right)
            help(n_stack, not right_first)
        help([root], right_first)
        return self.l
#others
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        level = [root]
        mark = True
        while level:
            if mark:
                res.append([p.val for p in level])
            else:
                res.append([p.val for p in level[::-1]])
            mark = not mark
            nextLevel = []
            for p in level:
                if p.left:
                    nextLevel.append(p.left)
                if p.right:
                    nextLevel.append(p.right)
            level = nextLevel
        return res
# Lesson
扫一遍和扫两遍的复杂度是一样的。
