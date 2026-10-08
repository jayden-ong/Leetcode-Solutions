class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # If all parentheses are closed, remove first and last
        beginning = 1
        num_open = 1
        length_s = len(s)
        curr = ""
        for i in range(1, length_s):
            if s[i] == "(":
                num_open += 1
            else:
                num_open -= 1
            
            if num_open == 0:
                curr += s[beginning:i]
                beginning = i + 2
                #print(curr)
        return curr