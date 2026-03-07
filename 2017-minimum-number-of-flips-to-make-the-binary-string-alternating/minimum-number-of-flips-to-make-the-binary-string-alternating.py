class Solution:
    def minFlips(self, s: str) -> int:
        ones_even = ones_odd = 0
        zeros_even = zeros_odd = 0
        for i, char in enumerate(s):
            if i % 2 == 0 and char == "1":
                ones_even += 1
            elif i % 2 == 1 and char == "1":
                ones_odd += 1
            elif i % 2 == 0 and char == "0":
                zeros_even += 1
            elif i % 2 == 1 and char == "0":
                zeros_odd += 1
        
        answer = min(ones_even + zeros_odd, ones_odd + zeros_even)
        # Throw char to the front
        '''
        ones_odd, ones_even = ones_even, ones_odd
        zeros_odd, zeros_even = zeros_even, zeros_odd
        return min(answer, min(ones_even + zeros_odd, ones_odd + zeros_even))
        '''
        for i in range(len(s) - 1):
            char = s[i]
            if char == "0":
                zeros_odd, zeros_even = zeros_even - 1, zeros_odd
                if len(s) % 2 == 1:
                    zeros_even += 1
                else:
                    zeros_odd += 1
                
                ones_odd, ones_even = ones_even, ones_odd
            else:
                ones_odd, ones_even = ones_even - 1, ones_odd
                if len(s) % 2 == 1:
                    ones_even += 1
                else:
                    ones_odd += 1
                
                zeros_odd, zeros_even = zeros_even, zeros_odd
            
            answer = min(answer, min(ones_even + zeros_odd, ones_odd + zeros_even))
        return answer
            
