class Solution:
    def minimumPushes(self, word: str) -> int:
        word_length = len(word)
        answer = 0
        curr = 1
        while word_length > 0:
            answer += min(8, word_length) * curr
            word_length -= min(8, word_length)
            curr += 1
        return answer