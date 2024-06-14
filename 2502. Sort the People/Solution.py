class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_dict = zip(heights, names)
        sorted_dict = sorted(heights_dict, reverse=True)
        return [name for height, name in sorted_dict]