class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def combinations(n, m, k_limit):
            answer = 1
            m = min(m, n - m)
            for i in range(1, m + 1):
                answer = answer * (n - i + 1) // i
                if answer > k_limit:
                    return k_limit + 1
            return answer
        partition = len(s) // 2
        buckets = [0] * 26

        for i in range(partition):
            buckets[ord(s[i]) - ord('a')] += 1
        
        def permutations(remainder):
            answer = 1
            for i in range(26):
                if buckets[i] == 0:
                    continue
                
                answer *= combinations(remainder, buckets[i], k)
                if answer > k:
                    break
                remainder -= buckets[i]
            return answer
        
        left_chars = []
        start = 1
        for pos in range(partition):
            for i in range(26):
                if buckets[i] == 0:
                    continue
                
                buckets[i] -= 1

                perms = permutations(partition - pos - 1)
                if start + perms > k:
                    left_chars.append(chr(i + ord('a')))
                    break
                
                buckets[i] += 1
                start += perms
        
        if len(left_chars) < partition:
            return ""
        
        mid = ""
        if len(s) % 2 == 1:
            mid = s[partition]
        
        left_string = "".join(left_chars)
        right_string = left_string[::-1]
        return left_string + mid + right_string