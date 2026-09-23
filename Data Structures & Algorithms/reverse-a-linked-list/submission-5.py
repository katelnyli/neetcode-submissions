# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ghost = ListNode(0)
        curr = head
        while curr != None:
            temp = ghost.next
            ghost.next = curr
            nxt = curr.next 
            curr.next = temp

            curr = nxt

        return ghost.next