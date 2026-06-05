class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wave_types = []
        for i in range(1000):
            left, mid, right = (i // 100) % 10, (i // 10) % 10, i % 10
            if (mid > max(left, right)) | (mid < min(left, right)):
                wave_types.append(i)
        
        def get_count(num, pattern):
            string_num = str(num)
            t = pattern < 100
            answer = 0
            for i in range(len(string_num) - 2):
                prev = int(string_num[:i] or 0)
                curr = int(string_num[i:i + 3])
                suffix = int(string_num[i + 3:] or 0)
                mult = 10 ** (len(string_num) - i - 3)
                num_ways = 0

                if curr > pattern:
                    num_ways = prev - t + 1
                elif curr == pattern:
                    num_ways = max(0, prev - t)
                    answer += suffix + 1
                else:
                    num_ways = max(0, prev - t)
                answer += num_ways * mult
            return answer

        def get_wave_count(num):
            if num < 100:
                return 0
            answer = 0
            for p in wave_types:
                answer += get_count(num, p)
            return answer

        return get_wave_count(num2) - get_wave_count(num1 - 1)