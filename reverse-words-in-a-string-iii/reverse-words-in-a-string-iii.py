class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(["".join(reversed(x)) for x in s.split(" ")])
