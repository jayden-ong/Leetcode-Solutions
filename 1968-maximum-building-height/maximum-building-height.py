class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        # Last building can only be as tall as number of buildings
        # best case scenario, all buildings increment by 1
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + (restrictions[i][0] - restrictions[i - 1][0]))
        for i in range(len(restrictions) - 2, 0, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + (restrictions[i + 1][0] - restrictions[i][0]))
        
        answer = 0
        for i in range(len(restrictions) - 1):
            answer = max(answer, ((restrictions[i + 1][0] - restrictions[i][0]) + restrictions[i][1] + restrictions[i + 1][1]) // 2)
        return answer