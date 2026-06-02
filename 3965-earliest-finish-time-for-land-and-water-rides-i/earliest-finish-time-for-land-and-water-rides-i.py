class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        answer = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # land first
                if landStartTime[i] + landDuration[i] < waterStartTime[j]:
                    answer = min(answer, waterStartTime[j] + waterDuration[j])
                else:
                    answer = min(answer, landStartTime[i] + landDuration[i] + waterDuration[j])
                
                # water first
                if waterStartTime[j] + waterDuration[j] < landStartTime[i]:
                    answer = min(answer, landStartTime[i] + landDuration[i])
                else:
                    answer = min(answer, waterStartTime[j] + waterDuration[j] + landDuration[i])
        return answer