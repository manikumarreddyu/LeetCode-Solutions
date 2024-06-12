
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)

        c1 = 0
        c2 = 0

        for i in range(n) :
            if nums1[i] in nums2 :
                c1 += 1
        for i in range(m) :
            if nums2[i] in nums1 :
                c2 += 1
                
        return [c1, c2]
        