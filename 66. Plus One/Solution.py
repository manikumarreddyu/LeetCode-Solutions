class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1]<9:
        #     digits[-1]=digits[-1]+1
        # else:
        #     digits[-1]=0
        #     digits[-2]=digits[-2]+1
        # return digits
        
        s0=""
        for i in digits:
            s0+=str(i)
        print(s0)
        n1=int(s0)
        print(n1)
        n2=n1+1
        print(n2)
        s1=str(n2)
        print(s1)
        l=[]
        for i in s1:
            l.append(int(i))
        return l
        