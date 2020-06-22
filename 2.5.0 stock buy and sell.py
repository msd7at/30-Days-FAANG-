#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cm=prices[0]
        profit=[]
        mp=0
        for i in range(len(prices)):
            cm=min(cm,prices[i])
            mp=max(mp,prices[i]-cm)
            profit.append(mp)
        print(profit)
        cm=prices[-1]
        mp=0
        tm=0
        for i in range(len(prices)-1,-1,-1):
            cm=max(cm,prices[i])
            mp=max(mp,cm-prices[i])
            tm=max(tm,mp+profit[i])
        return tm
