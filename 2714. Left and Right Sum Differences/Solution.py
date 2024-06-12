class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        left_sum = [0] * len(nums)
        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        right_sum = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]
        for i,j in zip(left_sum,right_sum):
            answer.append(abs(i-j))
        return answer