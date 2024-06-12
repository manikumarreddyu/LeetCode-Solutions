class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        s = bin(sum)
        return s[2:]