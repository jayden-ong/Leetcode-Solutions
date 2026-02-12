class Solution:
    def longestBalanced(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            sub_dict = defaultdict(int)
            for j in range(i, len(s)):
                sub_dict[s[j]] += 1
                target = None
                valid = True
                for char in sub_dict:
                    if target is None:
                        target = sub_dict[char]
                        continue
                    
                    if sub_dict[char] != target:
                        valid = False
                        break
                if valid:
                    answer = max(answer, j - i + 1)
        return answer
