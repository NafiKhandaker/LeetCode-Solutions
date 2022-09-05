# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            summand = l1.val + l2.val
        
            if summand >= 10:
                summand = summand - 10

                if l1.next:
                    l1.next.val = 1 + l1.next.val

                elif l2.next:
                    l2.next.val = 1 + l2.next.val

                else:
                    return ListNode(summand, ListNode(1, None))

            return ListNode(summand, self.addTwoNumbers(l1.next, l2.next))
        
        elif l1:
            summand = l1.val
            
            if summand >= 10:
                summand = summand - 10

                if l1.next:
                    l1.next.val = 1 + l1.next.val

                else:
                    return ListNode(summand, ListNode(1, None))

            return ListNode(summand, self.addTwoNumbers(l1.next, l2))
            
        elif l2:
            summand = l2.val

            if summand >= 10:
                summand = summand - 10

                if l2.next:
                    l2.next.val = 1 + l2.next.val

                else:
                    return ListNode(summand, ListNode(1, None))

            return ListNode(summand, self.addTwoNumbers(l1, l2.next))
            
        else:
            return None
        
        
        
