class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # pre[x] is the number of times the prefix sum "x" has appears so far
        # It can go from -len(nums) to len(nums) which is why its length is len(nums) * 2 + 1
        pre = [0] * (len(nums) * 2 + 1)
        pre[len(nums)] = 1
        count = len(nums)
        answer = presum = 0
        for i in range(len(nums)):
            if nums[i] == target:
                presum += pre[count]
                count += 1
                pre[count] += 1
            else:
                count -= 1
                presum -= pre[count]
                pre[count] += 1
            answer += presum
        return answer