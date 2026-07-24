class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_XOR_val = pow(2, math.floor(math.log(max(nums), 2)) + 1) - 1
        ones = set(nums)
        twos = set()
        threes = set()
        for num1 in nums:
            for num2 in ones:
                twos.add(num1 ^ num2)
        
        for num1 in nums:
            for num2 in twos:
                threes.add(num1 ^ num2)
        return len(threes)
