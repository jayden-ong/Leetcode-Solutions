class UnionFind:
    def __init__(self, num_entries):
        self.parent = [i for i in range(num_entries)]
        self.size = [1] * num_entries
    
    def find_parent(self, index):
        if index == self.parent[index]:
            return index
        self.parent[index] = self.find_parent(self.parent[index])
        return self.parent[index]
    
    def union(self, index1, index2):
        if self.size[index1] < self.size[index2]:
            self.parent[index1] = index2
            self.size[index1] += self.size[index2]
        else:
            self.parent[index2] = index1
            self.size[index2] += self.size[index1]
    
    def combine(self, index1, index2):
        parent1, parent2 = self.find_parent(index1), self.find_parent(index2)
        if parent1 == parent2:
            return True
        self.union(parent1, parent2)
        return False

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        union_find = UnionFind(len(grid) * len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if union_find.combine(i * len(grid[0]) + j, (i - 1) * len(grid[0]) + j):
                        return True
                
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if union_find.combine(i * len(grid[0]) + j, i * len(grid[0]) + j - 1):
                        return True
        return False