class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        colors_checked = set()
        answer = 0
        num_colors = len(colors)
        for i in range(num_colors):
            if colors[i] not in colors_checked:
                for j in range(i + 1, num_colors):
                    if colors[i] != colors[j]:
                        answer = max(answer, j - i)
            colors_checked.add(colors[i])

        return answer