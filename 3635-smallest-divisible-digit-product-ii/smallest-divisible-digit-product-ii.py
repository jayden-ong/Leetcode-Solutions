class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        curr_t = t
        for i in range(2, 10):
            while curr_t % i == 0:
                curr_t //= i
        
        if curr_t > i:
            return "-1"
        
        n = len(num)
        remainder = [0] * (n + 1)
        remainder[0] = t
        curr_pos = n - 1
        
        num_list = list(num)
        for i in range(n):
            if num_list[i] == "0":
                curr_pos = i
                break
            remainder[i + 1] = remainder[i] // math.gcd(remainder[i], int(num_list[i]))
        
        if remainder[n] == 1:
            return num
        
        for i in range(curr_pos, -1, -1):
            while True:
                num_list[i] = chr(ord(num_list[i]) + 1)
                if num_list[i] > "9":
                    break
                
                curr_t = remainder[i] // math.gcd(remainder[i], int(num_list[i]))
                k = 9

                for j in range(n - 1, i, -1):
                    while curr_t % k != 0:
                        k -= 1
                    curr_t //= k
                    num_list[j] = str(k)
                
                if curr_t == 1:
                    return "".join(num_list)
        
        answer = []
        curr_t = t
        for i in range(9, 1, -1):
            while curr_t % i == 0:
                answer.append(str(i))
                curr_t //= i
        
        answer_string = "".join(answer)
        padding = max(n + 1 - len(answer_string), 0)
        answer_string += "1" * padding
        return answer_string[::-1]