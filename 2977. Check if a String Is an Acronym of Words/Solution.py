class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # res = ""
        # for word in words:
        #     res += word[0]
        # return res==s
        if len(words) != len(s):
            return False
        for i, word in enumerate(words):
            if word[0] != s[i]:
                return False
        return True
        