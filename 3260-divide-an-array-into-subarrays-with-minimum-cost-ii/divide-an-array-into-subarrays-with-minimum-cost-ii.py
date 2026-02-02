class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # The distance between the first index of the second subarray and the first index of the 
        # last subarray can be at most dist

        # For any index "j" (the index that starts the second subarray), we want to know the k - 2
        # smallest elements that are within dist indices from "j"
        # There has to be at least k - 1 elements total
        smallest_sums = [float('inf')] * len(nums)
        valid_vals = []
        valid_indices = set()
        valid_sum = 0
        valid_length = 0
        invalid_vals = []
        invalid_indices = set()
        for i in range(1, len(nums) - k + 2):
            # "i" represents the index of the second subarray
            # valid_vals stores the values that are part of the smallest_sums for index i
            # invalid_vals are too large and will not be part of smallest_sums for index i
            if i == 1:
                for x in range(i + 1, i + 1 + dist):
                    if len(valid_vals) < k - 2:
                        heapq.heappush(valid_vals, (-nums[x], x))
                        valid_indices.add(x)
                        valid_length += 1
                        valid_sum += nums[x]
                    else:
                        if -valid_vals[0][0] <= nums[x]:
                            heapq.heappush(invalid_vals, (nums[x], x))
                            invalid_indices.add(x)
                        else:
                            element_removed, index_removed = heapq.heappop(valid_vals)
                            heapq.heappush(valid_vals, (-nums[x], x))
                            valid_indices.add(x)
                            valid_indices.remove(index_removed)
                            valid_sum += nums[x]
                            valid_sum += element_removed
                            heapq.heappush(invalid_vals, (-element_removed, index_removed))
                            invalid_indices.add(index_removed)
            else:
                # Remove from invalid_indices 
                if i in invalid_indices:
                    invalid_indices.remove(i)
                else:
                    valid_indices.remove(i)
                    valid_sum -= nums[i]
                    valid_length -= 1
                
                # Want to prune both valid_vals and invalid_vals
                while valid_vals and valid_vals[0][1] <= i:
                    _, _ = heapq.heappop(valid_vals)
                while invalid_vals and invalid_vals[0][1] <= i:
                    _, _ = heapq.heappop(invalid_vals)
                
                # New element to look at -- nums[i + dist]
                # First add it to invalid_vals
                if i + dist < len(nums):
                    heapq.heappush(invalid_vals, (nums[i + dist], i + dist))
                    invalid_indices.add(i + dist)
                
                # We want to remove from valid_vals and add to invalid_vals
                if valid_vals and invalid_vals and -valid_vals[0][0] > invalid_vals[0][0]:
                    old_element, old_index = heapq.heappop(valid_vals)
                    heapq.heappush(invalid_vals, (-old_element, old_index))
                    valid_sum += old_element
                    valid_indices.remove(old_index)
                    valid_length -= 1
                    invalid_indices.add(old_index)

                # We want to remove from invalid_vals and add to valid_vals
                while valid_length < k - 2:
                    new_element, new_index = heapq.heappop(invalid_vals)
                    heapq.heappush(valid_vals, (-new_element, new_index))
                    valid_sum += new_element
                    valid_indices.add(new_index)
                    valid_length += 1
                    invalid_indices.remove(new_index)
                """
                print(valid_vals)
                print(valid_indices)
                print(valid_sum)
                print(valid_length)
                print(invalid_vals)
                print(invalid_indices)
                print("---")
                """
            smallest_sums[i] = valid_sum + nums[i]
        # print(smallest_sums)
        
        # The min sum will always be a sum of k different values
        # Need to ensure that there are enough elements to form the k groups

        # Assume "i" is the current index we are at and everything including and before that is in group 1
        # "n" - "i" is the amount of elements left and it must be at least k - 1 elements
        answer = float('inf')
        return min(smallest_sums) + nums[0]
        '''
        for i in range(len(nums) - k + 1):
            # The first element will always be a part of the final answer
            # nums[i + 1] will be the first element of the second subarray
            for j in range(i + 1, len(nums) - k + 2):
                answer = min(answer, smallest_sums[j] + nums[0])
        
        return answer
        '''