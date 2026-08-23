class Solution:
    def sumGame(self, num: str) -> bool:
        first_sum = second_sum = 0
        first_var = second_var = 0
        for i, digit in enumerate(num):
            if digit == "?":
                if i < len(num) // 2:
                    first_var += 1
                else:
                    second_var += 1
            else:
                if i < len(num) // 2:
                    first_sum += int(digit)
                else:
                    second_sum += int(digit)
        
        return (first_var + second_var) == 1 or first_sum - second_sum != (second_var - first_var) * 9 // 2