class Robot:

    def __init__(self, width: int, height: int):
        self.top = height - 1
        self.right = width - 1
        self.pos = [0, 0]
        self.dir = "East"

    def step(self, num: int) -> None:
        rotation_direction = {"North" : "West", "East" : "North", "South" : "East", "West" : "South"}
        direction_to_step = {"North" : (1, 0), "East" : (0, 1), "South" : (-1, 0), "West" : (0, -1)}
        num_tiles = (self.top + 1) * 2 + (self.right + 1) * 2 - 4
        # If you hit an edge and you still have steps, left, you will move counterclockwise until you run out of step
        while num > 0:
            if self.dir == "North":
                steps_taken = min(num, self.top - self.pos[0])
                num -= steps_taken
                self.pos[0] += steps_taken
            elif self.dir == "South":
                steps_taken = min(num, self.pos[0])
                num = max(num - self.pos[0], 0)
                self.pos[0] -= steps_taken
            elif self.dir == "East":
                steps_taken = min(num, self.right - self.pos[1])
                num = max(num - (self.right - self.pos[1]), 0)
                self.pos[1] += steps_taken
            else:
                steps_taken = min(num, self.pos[1])
                num = max(num - self.pos[1], 0)
                self.pos[1] -= steps_taken
            
            if num > 0:
                # Want to figure out how many rotations we do around the area
                if num >= num_tiles:
                    num %= num_tiles
                else:
                    self.dir = rotation_direction[self.dir]

    def getPos(self) -> List[int]:
        return [self.pos[1], self.pos[0]]

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()