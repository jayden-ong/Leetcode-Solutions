class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # SOLVE LATER
        A = set()
        B = set()
        for i in range(len(img1)):
            for j in range(len(img2)):
                if img1[i][j] == 1:
                    A.add((i, j))
                if img2[i][j] == 1:
                    B.add((i, j))
        
        translations_found = defaultdict(int)
        answer = 0
        for (a1, a2) in A:
            for (b1, b2) in B:
                h_translation = b1 - a1
                v_translation = b2 - a2
                translations_found[(h_translation, v_translation)] += 1
                answer = max(answer, translations_found[(h_translation, v_translation)])
        return answer