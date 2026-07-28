class Solution:
    def smallestPalindrome(self, s: str) -> str:
        letters_freq = [0] * 26
        for letter in s:
            letters_freq[ord(letter) - ord('a')] += 1
        
        answer = ""
        middle_letter = None
        for i in range(len(letters_freq)):
            if letters_freq[i] % 2 == 1:
                middle_letter = chr(i + ord('a'))
            
            answer += (chr(ord('a') + i)) * (letters_freq[i] // 2)
        
        if middle_letter:
            return answer + middle_letter + answer[::-1]
        return answer + answer[::-1]