class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = sum_even = 0
        for i in range(n):
            sum_odd += 2 * i + 1
            sum_even += 2 * i + 2
        
        return math.gcd(sum_odd, sum_even)