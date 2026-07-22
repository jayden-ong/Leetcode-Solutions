'''
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        blocks = [('1', 1)]
        active = 0
        if s[0] == '1':
            active += 1
        
        curr_block = 1
        num_behind = 0
        curr, curr_count = s[0], 1
        index_to_block_num_behind = [(1, 0)]
        for i in range(1, len(s)):
            if s[i] == curr:
                curr_count += 1
                num_behind += 1
            else:
                num_behind = 0
                curr_block += 1
                blocks.append((curr, curr_count))
                curr = s[i]
                curr_count = 1
            index_to_block_num_behind.append((curr_block, num_behind))
            if s[i] == '1':
                active += 1
        blocks.append((curr, curr_count))
        blocks.append(('1', 1))
        def get_sub_blocks(left, right):
            curr_left_block = blocks[index_to_block_num_behind[left][0]]
            curr_right_block = blocks[index_to_block_num_behind[right][0]]
            if index_to_block_num_behind[left][0] == index_to_block_num_behind[right][0]:
                return [('1', 1), (curr_left_block[0], curr_right_block[1] - curr_left_block[1]), ('1', 1)]
            else:
                new_left_block = (curr_left_block[0], curr_left_block[1] - index_to_block_num_behind[left][1])
                new_right_block = (curr_right_block[0], index_to_block_num_behind[right][1] + 1)
                if index_to_block_num_behind[right][0] - index_to_block_num_behind[left][0] == 1:
                    return [('1', 1), new_left_block, new_right_block, ('1', 1)]
                curr = [('1', 1), new_left_block]
                for i in range(index_to_block_num_behind[left][0] + 1, index_to_block_num_behind[right][0]):
                    curr.append(blocks[i])
                curr.append(new_right_block)
                curr.append(('1', 1))
                return curr

        def solve(blocks):
            if len(blocks) <= 4 or len(blocks) == 5 and blocks[1][0] == '1':
                return active
            answer = 0
            actual_start = 2
            if blocks[1][0] == '1':
                actual_start = 3
            for i in range(actual_start, len(blocks) - 2, 2):
                answer = max(answer, active + blocks[i - 1][1] + blocks[i + 1][1])
            return answer

        answers_dict = {}
        answer = []
        for left, right in queries:
            if (left, right) not in answers_dict:
                sub_blocks = get_sub_blocks(left, right)
                answers_dict[(left, right)] = solve(sub_blocks)
            answer.append(answers_dict[(left, right)])
        return answer
'''
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [0] * (self.n << 2)

        if self.n:
            self.build(1, 0, self.n - 1)

    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = self.arr[l]
            return

        mid = (l + r) >> 1

        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, L: int, R: int) -> int:
        if L > R:
            return 0

        def _query(p: int, l: int, r: int) -> int:
            if L <= l and r <= R:
                return self.seg[p]

            mid = (l + r) >> 1
            res = 0

            if L <= mid:
                res = max(res, _query(p << 1, l, mid))

            if R > mid:
                res = max(res, _query(p << 1 | 1, mid + 1, r))

            return res

        return _query(1, 0, self.n - 1)


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        cnt1 = s.count("1")

        zeroBlocks = []
        blockLeft = []
        blockRight = []

        i = 0
        while i < n:
            st = i

            while i < n and s[i] == s[st]:
                i += 1

            if s[st] == "0":
                zeroBlocks.append(i - st)
                blockLeft.append(st)
                blockRight.append(i - 1)

        m = len(zeroBlocks)
        if (
            m < 2
        ):  # continuous 0 blocks less than 2 segments, return the answer directly
            return [cnt1] * len(queries)

        tmpSum = [zeroBlocks[i] + zeroBlocks[i + 1] for i in range(m - 1)]
        seg = SegmentTree(tmpSum)
        ans = []

        for l, r in queries:
            i = bisect_left(blockRight, l)
            j = bisect_right(blockLeft, r) - 1

            # at most 1 continuous block of 0s within the substring
            if i > m - 1 or j < 0 or i >= j:
                ans.append(cnt1)
                continue

            firstLen = (
                blockRight[i] - max(blockLeft[i], l) + 1
            )  # actual length of the first consecutive block of 0s in the substring

            lastLen = (
                min(blockRight[j], r) - blockLeft[j] + 1
            )  # actual length of the last consecutive block of 0s in the substring

            # exactly 2 consecutive 0 blocks within the substring
            if i + 1 == j:
                bestGain = firstLen + lastLen
                ans.append(cnt1 + bestGain)
                continue

            val1 = firstLen + zeroBlocks[i + 1]

            val2 = zeroBlocks[j - 1] + lastLen

            val3 = seg.query(i + 1, j - 2)

            bestGain = max(val1, val2, val3)

            ans.append(cnt1 + bestGain)

        return ans