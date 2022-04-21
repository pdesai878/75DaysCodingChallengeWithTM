# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=dummy=ListNode(0)
        carry=0
        s=0
        while l1 or l2:
            
            if l1 and l2:
                s=l1.val+l2.val+carry
                carry=s//10
                dummy.next=ListNode(s%10)
            elif l1:
                s=l1.val+carry
                carry=s//10
                dummy.next=ListNode(s%10)
            elif l2:
                s=l2.val+carry
                carry=s//10
                dummy.next=ListNode(s%10)
            else:
                break
            # print(dummy.val)
            dummy=dummy.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            dummy.next=ListNode(carry)
        return res.next
                