class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i, j, k in itertools.combinations(arr, 3):
            if abs(i-j) <= a and abs(j-k) <= b and abs(k-i) <= c:
                cnt +=1
        return cnt