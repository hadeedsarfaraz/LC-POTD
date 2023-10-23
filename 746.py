class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        if n <= 1:
            return 0
        if n == 2:
            return min(cost[0], cost[1])
        
        # Initialize an array to store the minimum cost to reach each step.
        dp = [0] * n
        
        # Base case: The minimum cost to reach the first and second steps is the cost of those steps.
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Calculate the minimum cost for each step from the third step to the top.
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        # Return the minimum cost of reaching the top, which is either the last step or the second-to-last step.
        return min(dp[-1], dp[-2])

