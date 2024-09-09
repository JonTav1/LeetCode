
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        #We are saving the next node, then pointing the current node 
        #"curr" to the previous node, essentially reversing the list.
        #to continue the loop, we make prev equal to curr, 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

            