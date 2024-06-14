class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        sm = 0
        while nums :
            p1, p2 = nums.pop(), nums.pop()
            print(p1,p2)
            sm += p2
            print(sm)
        return sm