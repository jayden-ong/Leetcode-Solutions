class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters_dict = {"b" : 0, "a" : 0, "l" : 0, "o" : 0, "n" : 0}
        for char in text:  
            if char in "balon":
                letters_dict[char] += 1
        
        num_balloons = float('inf')
        for char in "balon":
            # Need one
            if char in "ban":
                num_balloons = min(num_balloons, letters_dict[char])
            else:
                num_balloons = min(num_balloons, letters_dict[char] // 2)
        return num_balloons
        

