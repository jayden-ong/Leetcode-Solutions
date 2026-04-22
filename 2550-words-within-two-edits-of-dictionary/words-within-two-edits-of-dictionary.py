class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answer = []
        for query in queries:
            for word in dictionary:
                edits = 0
                valid = True
                for i in range(len(query)):
                    if query[i] != word[i]:
                        edits += 1
                    
                    if edits > 2:
                        valid = False
                        break
                
                if valid:
                    answer.append(query)
                    break
        return answer