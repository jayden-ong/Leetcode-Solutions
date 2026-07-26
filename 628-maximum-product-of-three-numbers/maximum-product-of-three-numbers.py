class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        num_nums = 0
        num_pos = 0
        num_neg = 0
        num_zero = 0
        for num in nums:
            num_nums += 1
            if num > 0:
                num_pos += 1
            elif num < 0:
                num_neg += 1
            else:
                num_zero += 1
        
        num_nums = len(nums)
        if num_nums == 3:
            return nums[0] * nums[1] * nums[2]
        
        nums.sort()
        # The max product will be the product of the three max (if all positive - NOT TRUE or negative) 
        if (num_pos >= 3 and num_neg <= 1) or (num_pos == 0 and num_zero == 0):
            return nums[-1] * nums[-2] * nums[-3]
        # If there is at least one positive and two negative, want to take their product
        elif num_pos >= 1 and num_neg >= 2:
            return max(nums[-1] * nums[0] * nums[1], nums[-3] * nums[-2] * nums[-1])
        # If there is at most 1 positive, result is either 0 or negative
        #elif num_pos <= 1 and num_zero >= 1:
        #    return 0
        else:
            return 0
        
