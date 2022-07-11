class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.lt =[k, nums]
    def add(self, val: int) -> int:
        self.lt[1].append(val)
        self.lt[1].sort()
        return self.lt[1][-self.lt[0]]
