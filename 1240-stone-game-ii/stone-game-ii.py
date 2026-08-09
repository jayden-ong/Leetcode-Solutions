class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo_dict = {}
        def determine_stones(curr_index, curr_m, remaining_points):
            if curr_index == len(piles):
                return 0
            
            if len(piles) - curr_index <= curr_m * 2:
                return remaining_points
            
            original_index = curr_index
            curr_points = 0
            max_points = float("-inf")
            for i in range(curr_m * 2):
                curr_points += piles[curr_index]
                remaining_points -= piles[curr_index]
                curr_index += 1
                if (curr_index, max(curr_m, i + 1)) in memo_dict:
                    other_player_max_points = memo_dict[(curr_index, max(curr_m, i + 1))]
                else:
                    other_player_max_points = determine_stones(curr_index, max(curr_m, i + 1), remaining_points)
                max_points = max(max_points, curr_points + remaining_points - other_player_max_points)
            
            memo_dict[(original_index, curr_m)] = max_points
            return max_points
            
        return determine_stones(0, 1, sum(piles))