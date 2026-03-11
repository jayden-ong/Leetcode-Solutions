class Solution:
    def bitwiseComplement(self, n: int) -> int:
        string_n = format(n, "b")
        length_n = len(string_n)
        curr_string = ""
        for i in range(length_n):
            if string_n[i] == "1":
                curr_string += "0"
            else:
                curr_string += "1"
        return int(curr_string, 2)