class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sm = 0
        while nums :
            p1, p2 = nums.pop(), nums.pop()
            sm += p2
        return sm