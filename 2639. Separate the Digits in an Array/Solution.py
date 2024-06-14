class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=""
        for i in nums:
            res+=str(i)
        re=[]
        for i in res:
            re.append(int(i) )
        return re

        