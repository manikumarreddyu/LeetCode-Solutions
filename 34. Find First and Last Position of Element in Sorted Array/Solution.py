class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            start = nums.index(target)
            end = start
            while end + 1 < len(nums) and nums[end + 1] == target:
                end += 1
            return [start, end]
        except ValueError:
            return [-1, -1]