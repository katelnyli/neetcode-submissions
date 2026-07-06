# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while head:
            nxt = head.next
            old_nxt = curr.next
            curr.next = head
            curr.next.next = old_nxt
            head = nxt

        return dummy.next

