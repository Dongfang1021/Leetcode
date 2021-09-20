class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower = -1 << 31
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True