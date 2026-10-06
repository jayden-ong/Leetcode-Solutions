class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_opening = 0
        num_closing = 0
        stack = []
        for paren in s:
            if len(stack) > 0 and paren == ")" and stack[-1] == "(":
                num_opening -= 1
                stack.pop()
            else:
                if paren == "(":
                    num_opening += 1
                else:
                    num_closing += 1
                stack.append(paren)
        
        if len(stack) == 0:
            return 0
        
        return num_opening + num_closing
                