class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letter_set = set()
        invalid_set = set()
        for letter in word:
            letter_set.add(letter)
            if letter.islower() and letter.upper() in letter_set:
                invalid_set.add(letter)
        
        answer = 0
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) in letter_set and chr(i).upper() in letter_set and chr(i) not in invalid_set:
                answer += 1
        return answer