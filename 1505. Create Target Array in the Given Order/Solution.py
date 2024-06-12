class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        #Iterate through nums and index simultaneously using 'zip'.
        for (num,idx) in zip(nums,index):
            #Insert num at index idx in target in each iteration.
            target.insert(idx,num)
        return target
        