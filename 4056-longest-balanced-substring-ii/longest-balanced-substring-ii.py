class Solution:
    def longestBalanced(self, s: str) -> int:
        # One character
        first, prev_char = 1, s[0]
        curr = 1
        for i in range(1, len(s) + 1):
            if i != len(s) and s[i] == prev_char:
                curr += 1
            else:
                first = max(first, curr)
                curr = 1
                if i != len(s):
                    prev_char = s[i]

        # Two characters
        # max diff between characters is 2 * n
        second = 0
        for x, y in [("a", "b"), ("a", "c"), ("b", "c")]:
            i = 0
            while i < len(s):
                while i < len(s) and s[i] != x and s[i] != y:
                    i += 1
                
                earliest = {}
                earliest[0] = i - 1
                curr_diff = 0
                while i < len(s) and (s[i] == x or s[i] == y):
                    if s[i] == x:
                        curr_diff += 1
                    else:
                        curr_diff -= 1
                        
                    if curr_diff in earliest:
                        second = max(second, i - earliest[curr_diff])
                    else:
                        earliest[curr_diff] = i
                    i += 1
                
        third = 0
        curr_a = curr_b = curr_c = 0
        earliest = {}
        earliest[(0, 0)] = -1
        for i in range(len(s)):
            if s[i] == "a":
                curr_a += 1
            elif s[i] == "b":
                curr_b += 1
            else:
                curr_c += 1
            
            diff1, diff2 = curr_a - curr_b, curr_a - curr_c
            if (diff1, diff2) in earliest:
                third = max(third, i - earliest[(diff1, diff2)])
            else:
                earliest[(diff1, diff2)] = i
        # Three characters
        return max([first, second, third])