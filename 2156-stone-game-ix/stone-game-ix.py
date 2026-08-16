class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        rem_one = rem_two = rem_zero = 0
        for stone in stones:
            if stone % 3 == 0:
                rem_zero += 1
            elif stone % 3 == 1:
                rem_one += 1
            else:
                rem_two += 1
        
        if rem_zero % 2 == 0:
            return rem_one >= 1 and rem_two >= 1
        return rem_one - rem_two > 2 or rem_two - rem_one > 2