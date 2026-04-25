class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        low = 1
        high = side
        new_points = [] 
        for x, y in points:
            if x == 0:
                new_points.append(y)
            elif x == side:
                new_points.append(3 * side - y)
            elif y == 0:
                new_points.append(4 * side - x)
            else:
                new_points.append(side + x)
        new_points.sort()

        # Want to use binary search to see if it is possible to choose k points with distance at least threshold
        def find_possible(threshold):
            for first in new_points:
                end = first + (side * 4) - threshold
                curr = first
                for _ in range(k - 1):
                    index = bisect_left(new_points, curr + threshold)
                    if index == len(new_points) or new_points[index] > end:
                        curr = -1
                        break
                    curr = new_points[index]
                if curr >= 0:
                    return True
            return False

        answer = 1
        while low <= high:
            mid = (low + high) // 2
            if find_possible(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer