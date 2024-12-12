class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        while(k!=0):
            gifts[gifts.index(max(gifts))] = int(math.sqrt(max(gifts)))
            k-=1
        return sum(gifts)
