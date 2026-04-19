class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0
        answer = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums1[i] <= nums2[j]:
                j += 1
            
            if 0 <= j - 1 < len(nums2) and nums1[i] <= nums2[j - 1]:
                answer = max(answer, j - 1 - i)
        return answer