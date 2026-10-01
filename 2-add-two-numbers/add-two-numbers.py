# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        current1 = l1
        current2 = l2
        carry = 0

        head = ListNode(0)
        currentSum = head
            
        while current1 is not None or current2 is not None:    
            if current1 is None:
                digit1 = 0
            else:
                digit1 = current1.val

            if current2 is None:
                digit2 = 0
            else:
                digit2 = current2.val

            sum = digit1 + digit2 + carry
            
            if sum > 9:
                carry = sum // 10
                sum = sum % 10
            else:
                carry = 0
            
            currentSum.val = sum

            if current1 is not None:
                current1 = current1.next
            if current2 is not None:
                current2 = current2.next

            if current1 is not None or current2 is not None:
                currentSum.next = ListNode(0)
                currentSum = currentSum.next

        if carry > 0:
            currentSum.next = ListNode(carry)

        return head