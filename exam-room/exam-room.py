class ExamRoom:

    def __init__(self, n: int):
        self.occupied = []
        self.n = n
        
    def seat(self) -> int:
        if not self.occupied:
            self.occupied.append(0)
            return 0
        left, right = -self.occupied[0], self.occupied[0]
        maximum = (right - left) // 2
        for start, end in zip(self.occupied, self.occupied[1:] + [2* self.n - 2 - self.occupied[-1]]):
            if (end - start) // 2 > maximum:
                left, right = start, end
                maximum = (right - left) //2
        bisect.insort(self.occupied, left + maximum)
        return left + maximum
    
    def leave(self, p: int) -> None:
        self.occupied.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
