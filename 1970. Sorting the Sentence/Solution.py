class Solution:
    def sortSentence(self, s: str) -> str:
        a=s[::-1].split()
        print(a)
        a.sort()
        print(a)
        r=[]  
        for word in a:
            r.append(word[1:][::-1])
            print(r)
        return " ".join(r)