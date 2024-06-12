class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a,2) + int(b,2)
        print(sum)
        s = bin(sum)
        print(s)
        return s[2:]