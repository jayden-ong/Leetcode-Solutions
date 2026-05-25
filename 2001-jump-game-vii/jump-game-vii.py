class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        end = 0

        while queue:
            i = queue.popleft()
            if s[i] == "0":
                if i == len(s) - 1:
                    return True
                
                for j in range(max(i + minJump, end + 1), min(i + maxJump + 1, len(s))):
                    queue.append(j)
                end = i + maxJump
        return False
        