class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)
        n = len(nums[0])
        def find_nums(curr_num):
            if len(curr_num) == n:
                if curr_num not in nums_set:
                    return (True, curr_num)
                return (False, "")

            for num in ["0", "1"]:
                res = find_nums(curr_num + num)
                if res[0]:
                    return res
            return (False, "")
        return find_nums("")[1]