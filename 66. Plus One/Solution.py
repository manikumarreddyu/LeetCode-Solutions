class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:    
        s0=""
        for i in digits:
            s0+=str(i)
        print(s0)
        n1=int(s0)
        n2=n1+1
        s1=str(n2)
        l=[]
        for i in s1:
            l.append(int(i))
        return l
        