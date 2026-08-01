class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        
        def get_diff(index1, index2):
            if index1 == index2:
                return nums[index1]
            
            return max(nums[index1] - get_diff(index1 + 1, index2), nums[index2] - get_diff(index1, index2 - 1))
        return get_diff(0, len(nums) - 1) >= 0