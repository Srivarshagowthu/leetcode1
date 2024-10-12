class Solution:
    def maxProfit(self, a: List[int]) -> int:
        prof=0
        for i in range(1,len(a)):
            if a[i]>a[i-1]:
                prof+=(a[i]-a[i-1])
        return prof