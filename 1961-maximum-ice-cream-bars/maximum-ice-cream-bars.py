class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        answer = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                answer += 1
            else:
                return answer
        return len(costs)