class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_dict = {}
        temp = arr.copy()
        temp.sort()
        rank = 1
        for num in temp:
            if num not in rank_dict:
                rank_dict[num] = rank
                rank += 1
        length_arr = len(arr)
        answer = [0] * length_arr
        for i in range(length_arr):
            answer[i] = rank_dict[arr[i]]
        return answer