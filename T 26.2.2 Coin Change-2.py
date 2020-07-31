#link:  https://leetcode.com/problems/coin-change-2/
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        a=[0 for k in range(amount+1)]
        a[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                a[j]+=a[j-coins[i]]
        return a[amount]
            
        
