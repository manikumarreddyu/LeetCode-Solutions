class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum=sum(nums)
        d=""
        for i in nums:
            d+=str(i)
        print(d)
        dig_sum=0
        for i in d:
            dig_sum+=int(i)
        return abs(ele_sum-dig_sum)

        