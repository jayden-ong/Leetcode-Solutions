# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        answer = float('-inf')
        for i in range(len(nums) // 2):
            answer = max(answer, nums[i] + nums[len(nums) - 1 - i])
        return answer