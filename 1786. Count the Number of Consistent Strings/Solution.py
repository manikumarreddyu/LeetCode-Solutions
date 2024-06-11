class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        a=set(allowed)
        
        for i in words:
            for j in i:
                if j not in allowed:
                    count+=1
                    break
        return len(words)-count

        