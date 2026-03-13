class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Keep track of when they'll be done
        times_heap = []
        for worker in workerTimes:
            heapq.heappush(times_heap, (worker, worker, 1))
        
        while mountainHeight > 0:
            worker_time, base_time, height_decreased = heapq.heappop(times_heap)
            mountainHeight -= 1
            height_decreased += 1
            heapq.heappush(times_heap, (worker_time + base_time * height_decreased, base_time, height_decreased))
        return worker_time
