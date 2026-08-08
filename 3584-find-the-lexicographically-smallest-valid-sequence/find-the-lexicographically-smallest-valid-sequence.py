class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        last_chance = [-1] * len(word2)
        j = len(word2) - 1
        for i in range(len(word1) - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last_chance[j] = i
                j -= 1
        
        answer = []
        can_skip = True
        j = 0
        for i, char in enumerate(word1):
            if j == len(word2):
                break
            
            if char == word2[j] or can_skip and (j == len(word2) - 1 or i < last_chance[j + 1]):
                answer.append(i)
                if char != word2[j]:
                    can_skip = False
                j += 1
        if j == len(word2):
            return answer
        return []