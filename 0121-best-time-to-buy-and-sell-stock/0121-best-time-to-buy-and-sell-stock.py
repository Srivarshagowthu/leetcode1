class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        i=0
        maxv=0
        for i in range(i+1,len(prices)):
            buy=min(prices[i],buy)
            prof=prices[i]-buy
            maxv=max(maxv,prof)
        return maxv
