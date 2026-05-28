class Node:
    def __init__(self):
        self.children, self.min_length, self.index = {}, float('inf'), float('inf')

class Tree:
    def __init__(self):
        self.root = Node()
    
    def insert(self, string, index):
        curr = self.root
        if len(string) < curr.min_length:
            curr.min_length = len(string)
            curr.index = index
        
        for char in string:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

            if len(string) < curr.min_length:
                curr.min_length = len(string)
                curr.index = index
    
    def query(self, string):
        curr = self.root

        for char in string:
            if char in curr.children:
                curr = curr.children[char]
            else:
                break
        
        return curr.index

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tree = Tree()

        for i, word in enumerate(wordsContainer):
            word_r = word[::-1]
            tree.insert(word_r, i)
        
        answer = []
        for query in wordsQuery:
            query_r = query[::-1]
            answer.append(tree.query(query_r))
        return answer