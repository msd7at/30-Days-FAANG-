# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
		# initialization for dp_table
        dp_table = [ float('inf') for _ in range(amount+1) ]
        
        # base case for $0
        dp_table[0] = 0
        
        for value in range(1, amount+1):
            for coin in coins:
                if coin > value:
					# coin value is to big, can not make change with current coin
                    continue
                
                # update dp_table, try to make change with coin
                dp_table[value] = min( (dp_table[value], dp_table[ value - coin ] + 1) )
        
        if dp_table[amount] != float('inf'):
            # Accept, return total count of coin change
            return dp_table[amount]
        else:
            # Reject, no solution
            return -1
