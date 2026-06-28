class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        answer = 1
        arr[0] = 1
        prev_unique_element = 1
        for i in range(1, len(arr)):
            if arr[i] == prev_unique_element:
                continue
            
            # Do not have to decrease
            if abs(arr[i] - prev_unique_element) <= 1:
                prev_unique_element = arr[i]
                answer = max(answer, arr[i])
                continue
            else:
                prev_unique_element = prev_unique_element + 1
                answer = max(answer, prev_unique_element)
        return answer