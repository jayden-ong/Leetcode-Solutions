class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliest_finish = float('inf')
        for i in range(len(landStartTime)):
            earliest_finish = min(earliest_finish, landStartTime[i] + landDuration[i])
        
        final_earliest_finish = float('inf')
        for j in range(len(waterStartTime)):
            final_earliest_finish = min(final_earliest_finish, max(earliest_finish, waterStartTime[j]) + waterDuration[j])
        
        curr_answer = final_earliest_finish

        earliest_finish = float('inf')
        for i in range(len(waterStartTime)):
            earliest_finish = min(earliest_finish, waterStartTime[i] + waterDuration[i])
        
        final_earliest_finish = float('inf')
        for j in range(len(landStartTime)):
            final_earliest_finish = min(final_earliest_finish, max(earliest_finish, landStartTime[j]) + landDuration[j])
        
        return min(final_earliest_finish, curr_answer)