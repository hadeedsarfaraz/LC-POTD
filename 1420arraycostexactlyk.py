class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        def count_ways(i, max_val, search_cost):
            if i == n:
                return 1 if search_cost == k else 0
            
            if search_cost > k or max_val > m:
                return 0
            
            if memo[i][max_val][search_cost] != -1:
                return memo[i][max_val][search_cost]
            
            total_ways = 0
            for v in range(1, m + 1):
                if v > max_val:
                    total_ways += count_ways(i + 1, v, search_cost + 1)
                else:
                    total_ways += count_ways(i + 1, max_val, search_cost)
                total_ways %= MOD
            
            memo[i][max_val][search_cost] = total_ways
            return total_ways
        
        memo = [[[-1 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
        
        return count_ways(0, 0, 0)
