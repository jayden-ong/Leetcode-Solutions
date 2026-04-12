class Solution:
    def minimumDistance(self, word: str) -> int:
        def find_distance(first_letter_num, second_letter_num):
            return abs(first_letter_num // 6 - second_letter_num // 6) + abs(first_letter_num % 6 - second_letter_num % 6)
        
        dp = [[[float('inf')] * 26 for _ in range(26)] for _ in range(len(word) + 1)]
        # The cost of the first char is always 0
        for l in range(26):
            for r in range(26):
                dp[0][l][r] = 0
            
        answer = float('inf')
        for i, letter in enumerate(word):
            curr_letter_num = ord(letter) - ord('A')

            for l in range(26):
                for r in range(26):
                    # Our fingers could be at any of the 26 letters, and we want to find the min distance to the next letter with either finger
                    dp[i + 1][l][curr_letter_num] = min(dp[i + 1][l][curr_letter_num], dp[i][l][r] + find_distance(r, curr_letter_num))
                    dp[i + 1][curr_letter_num][r] = min(dp[i + 1][curr_letter_num][r], dp[i][l][r] + find_distance(l, curr_letter_num))
                    
                    if i + 1 == len(word):
                        answer = min(answer, dp[len(word)][l][curr_letter_num])
                        answer = min(answer, dp[len(word)][curr_letter_num][r])
                    
        
        '''
        for l in range(26):
            for r in range(26):
                answer = min(answer, dp[len(word)][l][r])
        '''
        return answer