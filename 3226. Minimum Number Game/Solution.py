class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        alice=[]
        bob=[]
        for i in range(len(nums)):
            if i%2==0:
                alice.append(nums[i])
            else:
                bob.append(nums[i])
        print(alice)
        print(bob)
        ans=[]
        for i,j in zip(bob,alice):
            ans.append(i)
            ans.append(j)
        return ans
        