class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up_down = 0
        right_left = 0
        for move in moves:
            if move == 'U':
                up_down += 1
            elif move == 'D':
                up_down -= 1
            elif move == 'L':
                right_left -= 1
            elif move == 'R':
                right_left += 1
        return up_down == 0 and right_left == 0