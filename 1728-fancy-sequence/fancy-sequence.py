class Fancy:
    def __init__(self):
        self.vals = []
        self.MOD = pow(10, 9) + 7
        self.global_mult = 1
        self.global_add = 0

    def append(self, val: int) -> None:
        # Want to convert value into its base form
        start_val = (val - self.global_add + self.MOD) - self.MOD
        self.vals.append(start_val * pow(self.global_mult, self.MOD - 2, self.MOD) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.global_add = (self.global_add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.global_add = (self.global_add * m) % self.MOD
        self.global_mult = (self.global_mult * m) % self.MOD
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.vals[idx] * self.global_mult + self.global_add) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)