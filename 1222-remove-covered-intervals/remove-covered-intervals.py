class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        answer = 1
        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            # The prev interval includes the entire next interval because of the way intervals is sorted
            if prev_interval[0] <= intervals[i][0] < intervals[i][1] <= prev_interval[1]:
                continue
            prev_interval = intervals[i]
            answer += 1
        return answer