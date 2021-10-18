class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.cPow(1/x, abs(n))
        else:
            return self.cPow(x, n)
        
    def cPow(self, x, n):
        if n == 0:
            return 1
        a = self.cPow(x, n//2)
        if (n % 2 == 0):
            return a**2
        else:
            return x*(a**2)

        