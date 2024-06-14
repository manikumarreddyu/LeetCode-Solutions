class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0
        for i in range(k):
            res+=nums[-1]
            nums[-1]+=1
        return res
        