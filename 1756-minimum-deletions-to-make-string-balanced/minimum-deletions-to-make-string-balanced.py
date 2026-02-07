class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = []
        for i in range(len(s)):
            dp.append([0, 0])
        
        num_a_after = 0
        num_b_before = 0
        for i in range(len(s)):
            dp[i][1] = num_b_before
            if s[i] == "b":
                num_b_before += 1
            
            dp[len(s) - i - 1][0] = num_a_after
            if s[len(s) - i - 1] == "a":
                num_a_after += 1
        
        possible_answers = []
        num_deletions_forward = 0
        num_deletions_backward = 0
        for i in range(len(s)):
            if s[len(s) - i - 1] == "a":
                # We either have to get rid of all of those b's or get rid of the a
                if dp[len(s) - i - 1][1] > 0:
                    possible_answers.append(num_deletions_backward + dp[len(s) - i - 1][1])
                    num_deletions_backward += 1

            if s[i] == 'b':
                # We either have to get rid of all of those a's or get rid of the b
                if dp[i][0] > 0:
                    possible_answers.append(num_deletions_forward + dp[i][0])
                    num_deletions_forward += 1
        possible_answers.append(num_deletions_backward)
        possible_answers.append(num_deletions_forward)
        return min(possible_answers)
            