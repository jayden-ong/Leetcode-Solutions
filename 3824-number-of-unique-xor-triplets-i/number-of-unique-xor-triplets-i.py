class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        highest_bit = math.floor(math.log(len(nums), 2))
        return pow(2, highest_bit + 1)