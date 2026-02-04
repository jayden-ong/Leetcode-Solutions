class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # The entire decreasing part of the subarray has to be part of the answer
        # We want to find the largest possible sum for the two different parts of the increasing subarrays
        #   The first part must contain up to index p
        #       Use prefix sum -- take last val and subtract by smallest value up until then
        #   the second part must start with index q
        #       Use prefix sum -- take the max until the next decreasing part
        def find_part(curr_index, first_part):
            original_start = curr_index
            start_index = curr_index
            started_increasing = False
            curr, curr_min, third_curr = 0, 0, float('-inf')
            for i in range(start_index, len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    if not started_increasing:
                        started_increasing = True
                        curr = nums[i]
                        third_curr = nums[i] + nums[i + 1]
                    else:
                        curr_min = min(curr_min, curr)
                        curr += nums[i]
                        third_curr = max(third_curr, curr + nums[i + 1])
                elif nums[i] > nums[i + 1]:
                    if started_increasing:
                        break
                else:
                    # Need to reset everything because the next part cannot be decreasing
                    if first_part:
                        started_increasing, curr, curr_min, start_index, third_curr = False, 0, 0, i, float('-inf')
                    else:
                        break
                start_index += 1
            return (start_index, curr + nums[start_index] - curr_min, third_curr)
        
        answer = float('-inf')
        curr_index, first_part_max = 0, None
        # Want to find first increasing trionic subarray
        while curr_index < len(nums) - 1:
            # Need to find increasing part first
            if first_part_max is None or nums[curr_index] == nums[curr_index + 1]:
                curr_index, first_part_max, _ = find_part(curr_index, True)
            
            if curr_index == len(nums) - 1:
                break
            
            second_part = 0
            invalid = False
            while curr_index < len(nums) - 1 and nums[curr_index] >= nums[curr_index + 1]:
                if nums[curr_index] == nums[curr_index + 1]:
                    invalid = True
                    break
                second_part += nums[curr_index + 1]
                curr_index += 1
            
            # We cannot form a trionic array if the end of the decreasing sequence doesn't start increasing
            if curr_index == len(nums) - 1:
                break
            
            if invalid:
                continue
            # This val gets added twice in the final calculation because of "third_part_max"
            second_part -= nums[curr_index]
            
            curr_index, new_first_part_max, third_part_max = find_part(curr_index, False)
            answer = max(answer, first_part_max + second_part + third_part_max)
            first_part_max = new_first_part_max
        return answer
        