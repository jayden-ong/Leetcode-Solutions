class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def determinePrimeSetBits(num):
            string_num = format(num, "b")
            length_num = len(string_num)
            num_ones = 0
            for i in range(length_num):
                if string_num[i] == "1":
                    num_ones += 1
            if num_ones <= 1:
                return False

            for i in range(2, num_ones):
                if num_ones % i == 0:
                    return False
            return True
        
        answer = 0
        for i in range(left, right + 1):
            if determinePrimeSetBits(i):
                answer += 1
        return answer