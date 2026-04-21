class DisjointSet:
        def __init__(self, length):
            self.set = [i for i in range(length)]
        
        def find_rank(self, index):
            while self.set[index] != index:
                return self.find_rank(self.set[index])
            return self.set[index]
        
        def unite(self, index1, index2):
            first_parent = self.find_rank(index1)
            second_parent = self.find_rank(index2)
            self.set[second_parent] = first_parent

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        disjoint_set = DisjointSet(len(source))
        for first, second in allowedSwaps:
            disjoint_set.unite(first, second)
        
        parent_to_dictionary = {}
        index_to_parent = {}
        for i in range(len(source)):
            parent = disjoint_set.find_rank(i)
            index_to_parent[i] = parent
            if parent not in parent_to_dictionary:
                parent_to_dictionary[parent] = defaultdict(int)
            parent_to_dictionary[parent][source[i]] += 1

        answer = 0
        for i in range(len(source)):
            if parent_to_dictionary[index_to_parent[i]][target[i]] <= 0:
                answer += 1
            else:
                parent_to_dictionary[index_to_parent[i]][target[i]] -= 1
        return answer
                

