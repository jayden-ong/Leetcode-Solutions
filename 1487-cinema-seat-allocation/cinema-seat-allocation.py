class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)
        answer = 2 * n
        for (row, seat) in reservedSeats:
            if seat in (2, 3):
                seats[row].add(0)
            elif seat in (4, 5):
                seats[row].add(0)
                seats[row].add(1)
            elif seat in (6, 7):
                seats[row].add(1)
                seats[row].add(2)
            elif seat in (8, 9):
                seats[row].add(2)
        
        for row in seats:
            if len(seats[row]) == 3:
                answer -= 2
            else:
                answer -= 1
        return answer