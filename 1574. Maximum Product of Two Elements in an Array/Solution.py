class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=(sorted(nums))
        return (l[-1]-1)*(l[-2]-1)