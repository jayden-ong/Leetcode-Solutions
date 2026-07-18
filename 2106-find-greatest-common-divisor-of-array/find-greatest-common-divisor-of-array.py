class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = float('inf')
        largest = float('-inf')
        for num in nums:
            smallest = min(num, smallest)
            largest = max(num, largest)

        for i in range(smallest, 0, -1):
            if smallest % i == 0 and largest % i == 0:
                return i
        return 1