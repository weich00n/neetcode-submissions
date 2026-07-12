# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        dummy = ListNode(0, head)

        prev = dummy
        curr = head

        while l > n:
            prev = curr
            curr = curr.next
            l -= 1
        
        prev.next = curr.next

        return dummy.next
            
            

                