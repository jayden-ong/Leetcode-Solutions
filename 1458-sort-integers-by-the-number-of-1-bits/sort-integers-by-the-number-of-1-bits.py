class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(num):
            binary_num = format(num, "b")
            num_ones = 0
            for char in binary_num:
                if char == "1":
                    num_ones += 1
            return num_ones

        nums_dict = {}
        max_bits = 0
        for num in arr:
            num_bits = countBits(num)
            if num_bits in nums_dict:
                nums_dict[num_bits].append(num)
            else:
                nums_dict[num_bits] = [num]
            max_bits = max(max_bits, num_bits)
        
        answer = []
        for i in range(max_bits + 1):
            if i in nums_dict:
                curr_list = nums_dict[i]
                curr_list.sort()
                answer.extend(curr_list)
        return answer