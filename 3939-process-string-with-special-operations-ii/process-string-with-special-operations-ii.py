class Solution:
    def processStr(self, s: str, k: int) -> str:
        curr_length  = 0
        for char in s:
            if char == "*":
                curr_length  = max(curr_length  - 1, 0)
            elif char == "#":
                curr_length  *= 2
            elif char == "%":
                continue
            else:
                curr_length  += 1

        if k >= curr_length:
            return '.'
        
        for char in s[::-1]:
            if char == "*":
                curr_length += 1
            elif char == "#":
                if k >= (curr_length + 1) // 2:
                    k -= curr_length // 2
                curr_length = (curr_length + 1) // 2
            elif char == "%":
                k = curr_length - k - 1
            else:
                if k + 1 == curr_length:
                    return char
                curr_length -= 1
                continue
        return "."