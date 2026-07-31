class Solution:
    def minimumPushes(self, word: str) -> int:
        # First find the frequency of each letter
        letters_dict = {}
        for letter in word:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
        
        # Add to heap
        letters_heap = []
        for letter in letters_dict:
            heapq.heappush(letters_heap, (-letters_dict[letter], letter))
        
        # Want to determine how many letters are mapped to each key
        pushes_list = [1] * 8
        i = 0
        answer = 0
        while letters_heap:
            num_occur, curr_letter = heapq.heappop(letters_heap)
            num_occur *= -1
            answer += num_occur * pushes_list[i]
            pushes_list[i] += 1
            i = (i + 1) % 8
        return answer