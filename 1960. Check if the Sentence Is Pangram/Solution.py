class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=sorted(set(sentence))
        s1="abcdefghijklmnopqrstuvwxyz"
        res=""
        for i in s:
            res+=i
        return res==s1
        