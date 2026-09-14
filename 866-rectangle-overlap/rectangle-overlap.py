class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Other two corners are rec1[0] rec1[3], rec1[2] rec1[1]
        '''
        # Check rec1 corner over rec2 corner
        if rec1[0] > rec2[0] and rec1[0] < rec2[2] and rec1[1] > rec2[1] and rec1[1] < rec2[3]:
            return True
        
        if rec1[2] > rec2[0] and rec1[2] < rec2[2] and rec1[3] > rec2[1] and rec1[3] < rec2[3]:
            return True

        if rec1[0] > rec2[0] and rec1[0] < rec2[2] and rec1[3] > rec2[1] and rec1[3] < rec2[3]:
            return True
        
        if rec1[2] > rec2[0] and rec1[2] < rec2[2] and rec1[1] > rec2[1] and rec1[1] < rec2[3]:
            return True

        # Check rec2 corner over rec1 corner
        if rec2[0] > rec1[0] and rec2[0] < rec1[2] and rec2[1] > rec1[1] and rec2[1] < rec1[3]:
            return True
        
        if rec2[2] > rec1[0] and rec2[2] < rec1[2] and rec2[3] > rec1[1] and rec2[3] < rec1[3]:
            return True

        if rec2[0] > rec1[0] and rec2[0] < rec1[2] and rec2[3] > rec1[1] and rec2[3] < rec1[3]:
            return True
        
        if rec2[2] > rec1[0] and rec2[2] < rec1[2] and rec2[1] > rec1[1] and rec2[1] < rec1[3]:
            return True
        
        return False
        '''
        bottom1_y = min(rec1[1], rec1[3])
        top1_y = max(rec1[1], rec1[3])
        bottom2_y = min(rec2[1], rec2[3])
        top2_y = max(rec2[1], rec2[3])
        if bottom1_y >= top2_y or bottom2_y >= top1_y:
            return False
        
        bottom1_x = min(rec1[0], rec1[2])
        top1_x = max(rec1[0], rec1[2])
        bottom2_x = min(rec2[0], rec2[2])
        top2_x = max(rec2[0], rec2[2])
        if bottom1_x >= top2_x or bottom2_x >= top1_x:
            return False
        return True