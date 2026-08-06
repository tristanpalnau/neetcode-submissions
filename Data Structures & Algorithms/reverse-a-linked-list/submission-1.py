# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        cur = head
        address = {}
        i = 0
        while cur.next is not None:
            address[i] = cur
            cur = cur.next
            i += 1
        tail = cur
        for l in range(len(address)-1, -1, -1):
            cur.next = address[l] 
            cur = cur.next
        head.next = None
        return tail