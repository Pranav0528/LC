class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 != 0:
            high += 1
        

        return ((high)-(low-1))//2
        