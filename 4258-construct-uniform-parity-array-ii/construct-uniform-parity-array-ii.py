class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) % 2 == 1:
            return True
        
        all_even = True
        all_odd = True
        for num in nums1:
            if num % 2 == 1:
                all_even = False
            else:
                all_odd = False
            
            if not all_even and not all_odd:
                return False
        return True