class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = format(n, "b")
        length_n = len(bin_n)
        begin = None
        largest_distance = 0
        for i in range(length_n):
            if bin_n[i] == '1':
                if begin is None:
                    begin = i
                else:
                    largest_distance = max(largest_distance, i - begin)
                    begin = i
        return largest_distance