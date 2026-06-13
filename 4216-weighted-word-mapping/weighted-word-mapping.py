class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def get_word_sum(word):
            answer = 0
            for letter in word:
                answer += weights[ord(letter) - ord('a')]
            return answer
        
        answer = ""
        for word in words:
            word_sum = get_word_sum(word) % 26
            answer += chr(ord('z') - word_sum)
        return answer