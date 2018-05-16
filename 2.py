# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        root = l3
        indent = 0
        while True:
            if l1 == None and l2 == None and indent == 0:
                break
            if l1 != None:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2 != None:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            s = val1 + val2 + indent
            l3.next = ListNode(s%10)
            l3 = l3.next
            indent = s/10
        return root.next
