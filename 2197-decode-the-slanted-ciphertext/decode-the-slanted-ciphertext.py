class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Once we see a space, 
        answer = ""
        segments = defaultdict(list)
        curr_row = curr_col = 0
        num_columns = len(encodedText) // rows
        while curr_row < rows:
            for j in range(curr_col, num_columns):
                segments[j - curr_col].append(encodedText[curr_row * num_columns + j])
            curr_row += 1
            curr_col += 1
        
        for i in range(num_columns):
            answer += ''.join(segments[i])
        return answer.rstrip(" ")