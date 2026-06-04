class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def determine_waviness(num):
            curr = 0
            num_string = str(num)
            for i in range(1, len(num_string) - 1):
                if int(num_string[i - 1]) < int(num_string[i]) > int(num_string[i + 1]):
                    curr += 1
                elif int(num_string[i - 1]) > int(num_string[i]) < int(num_string[i + 1]):
                    curr += 1
            return curr

        answer = 0
        for num in range(max(num1, 100), num2 + 1):
            answer += determine_waviness(num)
        return answer