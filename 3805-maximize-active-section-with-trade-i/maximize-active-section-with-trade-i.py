class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        curr, curr_count = s[0], 1
        starting = curr
        active = 0
        if curr == '1':
            active += 1
        blocks = [1]
        for i in range(1, len(s)):
            char = s[i]
            if char == '1':
                active += 1
            
            if char == curr:
                curr_count += 1
            else:
                blocks.append(curr_count)
                curr = char
                curr_count = 1
        
        blocks.append(curr_count)
        blocks.append(1)

        if len(blocks) <= 4 or len(blocks) == 5 and starting == '1':
            return active
        
        actual_start = 2
        if starting == '1':
            actual_start = 3
        answer = 0
        for i in range(actual_start, len(blocks) - 2, 2):
            answer = max(answer, active + blocks[i - 1] + blocks[i + 1])
        return answer