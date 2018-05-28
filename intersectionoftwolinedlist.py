class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        """
        if the two linked lists have intersection, 
        and if you go through A + B vs B + A,
        you should see the intersection node at some point
        e.g. A: a1, a2, c1, c2, c3, B: b1, b2, b3, c1, c2, c3
        A -> B (link B to the end of A): a1, a2, c1, c2, c3, b1, b2, b3, c1, c2, c3
        B -> A (link A to the end of B): b1, b2, b3, c1, c2, c3, a1, a2, c1, c2, c3
        As you can see, the intersection is at c1 (the third element from the tail)
        If there's no intersection, the loop will exit because both pointer is None
        """

        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA

        return pa if pa is not None else None
