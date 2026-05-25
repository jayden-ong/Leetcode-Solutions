class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dq = deque([0])
        right = 0
        
        while dq:
            ix = dq.popleft()
            if s[ix] == '0':
                if ix == n-1:
                    return True
                curleft = ix + minJump
                curright = ix + maxJump
                for j in range(max(right+1, curleft), min(curright+1, n)):
                    dq.append(j)
                right = curright

        return False
        