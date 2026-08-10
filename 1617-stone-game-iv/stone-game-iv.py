class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        '''
        dp = {}
        def can_win(num_stones):
            if math.isqrt(num_stones) ** 2 == num_stones:
                return True
            
            if num_stones in dp:
                return dp[num_stones]
            
            for i in range(int(math.sqrt(num_stones)), 0, -1):
                if i ** 2 in dp:
                    curr_answer = dp[i ** 2]
                else:
                    curr_answer = not can_win(num_stones - i ** 2)
                
                if curr_answer:
                    return True
            return False
        return can_win(n)
        '''
        dp = defaultdict(bool)
        for i in range(n + 1):
            if dp[i]:
                continue
            
            for j in range(1, math.isqrt(n - i) + 1):
                dp[i + j * j] = True
            
            if dp[n]:
                return True
        
        return False
