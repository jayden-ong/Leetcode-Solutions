class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        highest = 0
        for change in gain:
            curr_alt += change
            highest = max(curr_alt, highest)
        return highest