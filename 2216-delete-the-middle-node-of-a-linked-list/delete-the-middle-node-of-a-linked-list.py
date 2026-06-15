# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        mid_index = length // 2
        if mid_index == 0:
            return None
        
        curr_index = 0
        curr = head
        for i in range(mid_index - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head