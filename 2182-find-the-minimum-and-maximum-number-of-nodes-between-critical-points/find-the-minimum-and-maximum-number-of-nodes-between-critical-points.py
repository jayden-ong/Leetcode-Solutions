# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Want to store the previous critical point
        prev_closest = None
        curr_closest = float('inf')
        # Want to store the earliest and latest critical point
        early_critical = None
        late_critical = None
        prev_val = head.val
        curr = head.next
        i = 1
        while curr is not None and curr.next is not None:
            if (prev_val < curr.val and curr.val > curr.next.val) or (prev_val > curr.val and curr.val < curr.next.val):
                if early_critical is None:
                    early_critical = i
                else:
                    late_critical = i
                
                if prev_closest is not None:
                    curr_closest = min(curr_closest, i - prev_closest)
                prev_closest = i

            prev_val = curr.val
            curr = curr.next
            i += 1
        
        if curr_closest == float('inf') or early_critical is None or late_critical is None:
            return [-1, -1]
        return [curr_closest, late_critical - early_critical]
